#!/usr/bin/python3
"""This module defines `validUTF8`"""


def validUTF8(data):
    """ Check is a list of integers is valid UTF-8 encoded data
        Return: True if data is valid UTF-8 encoded, else return False
    """
    if not all(isinstance(i, int) for i in data):
        return False
    # if not all(0 <= i < 256 for i in data):
    #     return False
    try:
        bytes(data).decode('utf-8')
        return True
    except (OverflowError, TypeError, UnicodeDecodeError, ValueError):
        return False


if __name__ == "__main__":
    data = [467, 133, 108]
    print(validUTF8(data))
