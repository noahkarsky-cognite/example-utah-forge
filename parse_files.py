"""
Common methods and classes to parse DLIS and LAS files
"""
from numpy import isnan


class FileReadError(Exception):
    pass


class FileConvertError(Exception):
    pass


def is_null(data):
    """
    Determine if a given value is NaN or non-convertible to floating number.
    """
    try:
        return isnan(float(data))
    except:
        return True


def clean_row(curve, nan):
    return [nan if is_null(element) else float(element) for element in curve]