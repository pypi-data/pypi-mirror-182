from typing import Optional

from aishield.connection import RequestProcessor
from aishield.constants import (
    FileFormat,
    ReportType,
    Attack,
    Task,
    ResponseStatus
)
from aishield.configs import (
    OutputConf,
    JobDetails
)
from aishield.image_classification import (
    extraction
)
from aishield.utils.util import (
    uri_validator,
    get_all_keys_by_val
)


class VulnConfig:
    """
    Instantiates the vulnerability configs based on task and attack type
    """

    def __new__(cls, task_type: Optional[Task] = Task.IMAGE_CLASSIFICATION,
                analysis_type: Optional[Attack] = Attack.EXTRACTION,
                defense_generate: Optional[bool] = True):
        """
        Return the Vulnerability Config object

        Parameters
        ----------
        task_type: Type of task. Example: Image Classification, Image Segmentation, NLP, etc.
        analysis_type: Type of analysis_type(attack) for which vulnerability assessment has to be done.Example: Extraction, Evasion,etc.
        defense_generate: Boolean flag to specify if defense needs to be generated if model found to be vulnerable

        Returns
        -------
        vul_config_obj : Class Object
        """
        task_type_val = task_type.value
        attack_val = analysis_type.value
        if task_type_val not in Task.valid_types():
            raise ValueError('task_type param value {} is not in one of the accepted values {}.'.format(task_type_val,
                                                                                                        Task.valid_types()))
        if attack_val not in Attack.valid_types():
            raise ValueError('attack param value {} is not in one of the accepted values {}.'.format(attack_val,
                                                                                                     Attack.valid_types()))

        if task_type == Task.IMAGE_CLASSIFICATION:
            if analysis_type == Attack.EXTRACTION:
                vul_config_obj = extraction.VulnConfig(defense_generate)
            elif analysis_type == Attack.EVASION:
                raise NotImplementedError('Feature coming soon')
            else:
                raise NotImplementedError('Feature coming soon')
        elif task_type == 'tsf':
            raise NotImplementedError('Feature coming soon')
        elif task_type == 'nlp':
            raise NotImplementedError('Feature coming soon')
        elif task_type == 'image_segmentation':
            raise NotImplementedError('Feature coming soon')
        else:
            raise NotImplementedError('New task-pairs would be added soon')
        return vul_config_obj


class AIShieldApi:
    """
    Instantiates for performing vulnerability analysis
    """

    def __init__(self, api_url: str, api_key: str, org_id: str):
        """
        Initializes the AIShield API with request headers

        Parameters
        ----------
        api_url: api endpoint of AIShield vulnerability analysis
        api_key: user api key
        org_id: organization key
        """
        if not api_url:
            raise ValueError('AIShield api is not provided')
        if not api_key:
            raise ValueError('api_key is not provided')
        if not org_id:
            raise ValueError('org_id is not provided')
        if not uri_validator(api_url):
            raise ValueError('aishield api is invalid')

        headers = {
            'Cache-Control': 'no-cache',
            'x-api-key': api_key,
            'Org-Id': org_id
        }
        self.request_processor = RequestProcessor(api_url, headers)

    def register_model(self, task_type: Optional[Task] = Task.IMAGE_CLASSIFICATION,
                       analysis_type: Optional[Attack] = Attack.EXTRACTION):
        """
            Perform the initial model registration process for vulnerability analysis

            Parameters
            ----------
            task_type: Type of task. Example: Image Classification, Image Segmentation, NLP, etc.
            analysis_type: Type of analysis_type(attack) for which vulnerability assessment has to be done.Example: Extraction, Evasion,etc.

            Returns
            -------
            status: registration status: success or failed
            job_details: having information of model_id, data_upload_uri, label_upload_uri, model_upload_uri
        """
        model_registration_payload = {
            'task_type': task_type,
            "analysis_type": analysis_type
        }
        status, job_details = self.request_processor.register(payload=model_registration_payload)
        return status, job_details

    def upload_input_artifacts(self, job_details: JobDetails, data_path: str = None, label_path: str = None,
                               model_path: str = None):
        """
            Upload the input artifacts such as data, label and model file

            Parameters
            ----------
            job_details: object having information such as model_id, data_upload_uri, label_upload_uri, model_upload_uri
            data_path: location of data file
            label_path: location of label file
            model_path: location of model file

            Returns
            -------
            upload_status_msg: all upload messages in a list
        """
        upload_status_msg = []
        if data_path:
            data_upload_uri = job_details.data_upload_uri
            upload_status = self.request_processor.upload_file(data_path=data_path, upload_uri=data_upload_uri)
            if upload_status == ResponseStatus.SUCCESS:
                upload_status_msg.append('data file upload successful')
            else:
                upload_status_msg.append('data file upload failed')
        if label_path:
            label_upload_uri = job_details.label_upload_uri
            upload_status = self.request_processor.upload_file(data_path=label_path, upload_uri=label_upload_uri)
            if upload_status == ResponseStatus.SUCCESS:
                upload_status_msg.append('label file upload successful')
            else:
                upload_status_msg.append('label file upload failed')

        if model_path:
            model_upload_uri = job_details.model_upload_uri
            upload_status = self.request_processor.upload_file(data_path=model_path, upload_uri=model_upload_uri)
            if upload_status == ResponseStatus.SUCCESS:
                upload_status_msg.append('model file upload successful')
            else:
                upload_status_msg.append('model file upload failed')
        return upload_status_msg

    def vuln_analysis(self, model_id: str = None, vuln_config: VulnConfig = None):
        """
        Perform Vulnerability analysis of the model

        Parameters
        ----------
        model_id: model id obtained after model registration
        vuln_config: configs for vulnerability analysis of VulnConfig type

        Returns
        -------
        status: job status: success or failed
        job_details: having information such as job_id, monitoring link
        """

        payload = {key: getattr(vuln_config, key) for key in dir(vuln_config) if not key.startswith('_')}

        # validation - raise error any key in payload has None value
        keys_with_none_val = get_all_keys_by_val(payload, None)
        if keys_with_none_val:
            raise ValueError('None values found for {}.'.format(', '.join(keys_with_none_val)))

        task_type = vuln_config.task_type
        attack_strategy = vuln_config.attack

        if task_type == Task.IMAGE_CLASSIFICATION:
            if attack_strategy == Attack.EXTRACTION:
                va_extraction = extraction.VulnAnalysis(model_id, payload)
                payload = va_extraction.prep_analysis_payload()
            else:
                raise NotImplementedError('Feature coming soon')
        elif task_type == Task.TIMESERIES_FORECAST:
            raise NotImplementedError('Feature coming soon')

        elif task_type == Task.NLP:
            raise NotImplementedError('Feature coming soon')

        elif task_type == Task.IMAGE_SEGMENTATION:
            raise NotImplementedError('Feature coming soon')

        else:
            raise NotImplementedError('New task-pairs would be added soon')

        # Update payload
        del payload['task_type']
        del payload['attack']

        status, job_details = self.request_processor.send_for_analysis(payload=payload)
        return status, job_details

    def job_status(self, job_id):
        """
        Prints the status of each vulnerability analysis while the job is running.
        Once job completes, returns with status: success or failed

        Parameters
        ----------
        job_id: job_id returned from the request

        Returns
        -------
        status: success or failed
        """
        status = self.request_processor.get_job_status(job_id=job_id)
        return status

    def save_job_report(self, job_id: str = None, output_config: OutputConf = None) -> str:
        """
        Save the artifacts of the vulnerability analysis.

        Parameters
        ----------
        job_id: job_id returned from the request
        output_config: object with OutputConf Type

        Returns
        -------
        saved_loc: location where the artifact got saved.
        """
        if not job_id or job_id is None:
            raise ValueError('invalid job id value')
        file_format = output_config.file_format.value.lower()
        report_type = output_config.report_type.value.lower()
        save_folder_path = output_config.save_folder_path

        if file_format not in FileFormat.valid_types():
            raise ValueError('invalid file_format value {}. Must be one of {}'.format(file_format,
                                                                                      FileFormat.valid_types()))
        if report_type not in ReportType.valid_types():
            ValueError('invalid report_type value {}. Must be one of {}'.format(report_type,
                                                                                ReportType.valid_types()))
        saved_loc = self.request_processor.get_artifacts(job_id=job_id, report_type=report_type,
                                                         file_format=file_format,
                                                         save_folder_path=save_folder_path)
        return saved_loc
