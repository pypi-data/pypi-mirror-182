import os
from urllib.parse import urlparse
from inspect import getmembers
from types import FunctionType


def check_valid_filepath(filepath: str) -> bool:
    """
        Check if a file exists and is readable
        Parameters
        ----------
        filepath: location of the file

        Returns
        -------
        valid: True if a file exists in the specified path and is readable; otherwise False
    """

    valid = False
    if os.path.isfile(filepath) and os.access(filepath, os.R_OK):
        valid = True
    return valid


def get_all_keys_by_val(dictionary: dict, value) -> list:
    """
    Get all keys of a dictionary by its value
    Parameters
    ----------
    dictionary: dictionary object
    value: value to be compared with the values of dictionary

    Returns
    -------
    found_keys: keys that matches the provided value
    """
    found_keys = []
    for key, val in dictionary.items():
        if val == value:
            found_keys.append(key)
    return found_keys


def get_class_attributes(class_obj):
    """
    Gets the attributes of a class
    Parameters
    ----------
    class_obj: object of a class

    Returns
    -------
    The attributes of a class from the instantiated class object
    """
    disallowed_names = {
        name for name, value in getmembers(type(class_obj))
        if isinstance(value, FunctionType)}
    return {
        name: getattr(class_obj, name) for name in dir(class_obj)
        if name[0] != '_' and name not in disallowed_names and hasattr(class_obj, name)}


def uri_validator(url) -> bool:
    """
    check if the uri is valid
    Parameters
    ----------
    url: uri

    Returns
    -------
    valid: True or False
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False
