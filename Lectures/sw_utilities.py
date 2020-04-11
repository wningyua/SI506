import json
import requests


def convert_string_to_int(value):
    """Attempts to convert a string to an int.  If unsuccessful returns
    the value unchanged. Note that this function will return True for
    boolean values, faux string boolean values (e.g., "true"), "NaN",
    exponential notation, etc. See:
    https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int

    Parameters:
        value (str): string to be converted.

    Returns:
        int: if string successfully converted.
        str: if string could not be converted.

    """

    try:
        return int(value)
    except ValueError:
        return value


def convert_string_to_list(value, delimiter):
    """
    Splits a string using the provided delimiter.

    Parameters:
        value (str): string to be split.
        delimiter (str): delimiter used to split the string.

    Returns:
         list: a string converted to a list.

    """

    try:
        return value.split(delimiter)
    except AttributeError:
        return value


def filter_data(data, filter_keys):
    """Applies a key filter to a dictionary in order to return a subset of
    the key-values. The insertion order of the filtered key-value pairs is
    determined by the filter key sequence.

    Parameters:
        data (dict): key-value pairs to be filtered.
        filter_keys (tuple): sequence of key names that are used to select
                             key-value pairs that match on the key name.

    Returns:
        dict: filtered collection of key-value pairs.
    """

    return {key: data[key] for key in filter_keys if key in data.keys()}

    # record = {}
    # for key in filter_keys:
    #     if key in data.keys():
    #         record[key] = data[key]

    # return record


def get_swapi_resource(url, params=None, timeout=20):
    """Description removed. For you to write.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        response = requests.get(url, params=params, timeout=timeout).json()
    else:
        response = requests.get(url, timeout=timeout).json()

    return response


def is_unknown(value):
    """Check if value is in list of unknown values. If value
    is not a string catch the AttributeError raised by use of
    str.lower() and return False.
    """

    unknown_values = ('unknown', 'n/a')

    try:
        return value.lower() in unknown_values # truth value
    except AttributeError:
        return False


def read_json(filepath):
    """Description removed. For you to write.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict: dictionary representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data


def split_era_year(galatic_date):
    """Separate the Galatic date into era (e.g., BBY, ABY) and year.

    Parameters:
        galatic_date (str): Galatic year and era (e.g., 19BBY)

    Returns:
        tuple: era, year

    """

    return galatic_date[-3:], float(galatic_date[:-3]) # pack
