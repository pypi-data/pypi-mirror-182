import json
import os
import time
from datetime import datetime
import requests

from aishield.configs import JobDetails
from aishield.utils.exceptions import AIShieldException
from aishield.utils import logger
from aishield.utils.util import check_valid_filepath
from aishield.constants import ResponseStatus

LOG = logger.getLogger(__name__)


class RequestProcessor:
    def __init__(self, api_endpoint, headers):
        """
        Initialize with the api endpoint and headers required for calling to AIShield API
        Parameters
        ----------
        api_endpoint: api endpoint of AIShield vulnerability analysis
        headers: headers for the request
        """
        self.api_endpoint = api_endpoint
        self.headers = headers
        self.job_details = JobDetails()

    def register(self, payload):
        """
            Sends HTTP Post request to api_endpoint for model registration.
            Parameters
            ----------
            payload: task and analysis type as as JSON.

            Returns
            -------
            the status of job with details having model_id, data_upload_uri, label_upload_uri, model_upload_uri
            raises AIShieldException in case of errors or if the response from server does not indicate 'SUCCESS'.
        """
        model_registration_url = self.api_endpoint + "/AIShieldModelRegistration/v1.5"
        status = 'failed'
        try:
            response = requests.post(url=model_registration_url, params=payload, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException as e:
            raise AIShieldException(e)

        resp_json = None

        try:
            resp_json = response.json()
        except ValueError:
            raise AIShieldException(
                'Error response from server: {}{}'.format(
                    response.text[0:150], len(response.text) > 150 and '...' or ''
                )
            )
        if 'Data' in resp_json:
            status = 'success'
            self.job_details.model_id = resp_json['Data']['ModelID']
            self.job_details.data_upload_uri = resp_json['Data']['DataUploadURL']
            self.job_details.label_upload_uri = resp_json['Data']['LabelUploadURL']
            self.job_details.model_upload_uri = resp_json['Data']['ModelUploadURL']

        return status, self.job_details

    def upload_file(self, data_path, upload_uri):
        """
        Upload file to a particular uri for vulnerability analysis.
        Parameters
        ----------
        data_path: location of data file
        upload_uri : uri where file to be uploaded

        Returns
        -------
        the status of job with details
        raises AIShieldException in case of errors or if the response from server does not indicate 'SUCCESS'.
        """
        if not check_valid_filepath(data_path):
            raise FileNotFoundError('file at {} not found or not accessible'.format(data_path))
        try:
            data = open(data_path, 'rb')
            response = requests.request(method="PUT", url=upload_uri, data=data)
            response.raise_for_status()
        except requests.RequestException as e:
            raise AIShieldException(e)

        status_cd = response.status_code
        if status_cd == 200:
            status = ResponseStatus.SUCCESS
        else:
            status = ResponseStatus.FAILED
        return status

    def send_for_analysis(self, payload):
        """
        Sends HTTP Post request to api_endpoint for vulnerability analysis.
        Parameters
        ----------
        payload: dictionary, which is sent as as JSON.

        Returns
        -------
        the status of job with details
        raises AIShieldException in case of errors or if the response from server does not indicate 'SUCCESS'.
        """
        status = 'failed'
        model_analysis_url = self.api_endpoint + "/AIShieldModelAnalysis/v1.5"
        try:
            response = requests.post(url=model_analysis_url, params=payload, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException as e:
            raise AIShieldException(e)

        resp_json = None

        try:
            resp_json = response.json()
        except ValueError:
            raise AIShieldException(
                'Error response from server: {}{}'.format(
                    response.text[0:150], len(response.text) > 150 and '...' or ''
                )
            )
        if 'job_id' in resp_json:
            status = 'success'
            self.job_details.job_id = resp_json['job_id']
            self.job_details.job_monitor_uri = resp_json['monitor_link']

        return status, self.job_details

    def get_job_status(self, job_id) -> str:
        """
        Monitor progress for job id

        Parameters
        ----------
        job_id: id of the submitted job

        Returns
        -------
        Logs the status of individual steps of analysis and returns the final status of the task
        """
        job_status_url = self.api_endpoint + "/AIShieldModelAnalysis/" + "JobStatusDetailed?JobID=" + job_id
        status_dictionary = {
            'ModelExploration_Status': 'na',
            'SanityCheck_Status': 'na',
            'QueryGenerator_Status': 'na',
            'VunerabilityEngine_Status': 'na',
            'DefenseReport_Status': 'na',
        }
        failed_api_hit_count = 0
        LOG.info('Fetching job details for job id {}'.format(job_id))
        while True:
            time.sleep(5)
            try:
                job_status_response = requests.request("GET", job_status_url, headers=self.headers, timeout=15)
                job_status_payload = json.loads(job_status_response.text)
            except requests.RequestException as error:
                failed_api_hit_count += 1
                print("Error {}. retrying count {}  ...".format(error, failed_api_hit_count))
                if failed_api_hit_count >= 3:
                    raise AIShieldException(error)

            final_status = 'failed'
            failing_key = ''
            for key in status_dictionary.keys():
                if status_dictionary[key] == 'na':
                    if job_status_payload[key] == 'completed' or job_status_payload[key] == 'passed':
                        status_dictionary[key] = job_status_payload[key]
                        LOG.info(str(key) + ":" + status_dictionary[key])
                        print('running...', end='\r')
                    elif job_status_payload[key] == 'failed':
                        failing_key = key
                        status_dictionary[key] = job_status_payload[key]
                        LOG.info(str(key) + ":" + status_dictionary[key])
                        print('running...', end='\r')

            if failing_key and status_dictionary[failing_key] == 'failed':
                break

            if status_dictionary['VunerabilityEngine_Status'] == 'passed' or status_dictionary[
                'VunerabilityEngine_Status'] == 'completed' and job_status_payload[
                'CurrentStatus'] == "Defense generation is not triggered":
                LOG.info("\n Vulnerability score {} failed to cross vulnerability threshold of {}".format(
                    job_status_payload['VulnerabiltyScore']))
                final_status = 'success'
                break
            if job_status_payload['DefenseReport_Status'] == 'completed':
                final_status = 'success'
                break
        print('job run completed')
        LOG.info('Analysis completed for job id {}'.format(job_id))
        return final_status

    def get_artifacts(self, job_id, report_type, file_format, save_folder_path) -> str:
        """
        Get the artifacts like reports, attack samples or defense model

        Parameters
        ----------
        job_id: id of the submitted job
        report_type: type of report/artifact to be fetched
        file_format: format in which the file to be saved
        save_folder_path: folder path where the artifact will be saved

        Returns
        -------
        file_path: path of saved report/artifact
        """
        if report_type.lower() in ['vulnerability', 'defense']:
            if file_format == 'txt':
                file_format_id = 1
            elif file_format == 'pdf':
                file_format_id = 2
            elif file_format == 'json':
                file_format_id = 3
            elif file_format == 'xml':
                file_format_id = 4
            else:
                file_format_id = 0
                file_format = 'zip'  # all reports zipped
        if report_type.lower() in ['defense_artifact', 'attack_samples']:
            file_format_id = 0
            file_format = 'zip'

        job_artifact_url = self.api_endpoint + "/AIShieldModelAnalysis/" +\
                           "GetReport?JobID={}&ReportType={}&FileFormat={}".format(job_id, report_type, file_format_id)
        try:
            job_status_response = requests.request("GET", job_artifact_url, params={}, headers=self.headers)
        except requests.RequestException as error:
            raise AIShieldException(error)

        time_now = datetime.now().strftime("%Y%m%d_%H%M")
        file_name = '{}_{}.{}'.format(report_type, time_now, file_format)
        file_path = os.path.join(save_folder_path, file_name)
        with open(file_path, "wb") as f:
            f.write(job_status_response.content)
        LOG.info('{} is saved in {}'.format(file_name, save_folder_path))
        return file_path
