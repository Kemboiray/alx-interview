#!/usr/bin/python3
"""This module defines the function `validUTF8`"""


def to_bin(num):
    """Return formatted binary representation of `num`"""
    return format(num, "#010b")[-8:]


def validUTF8(data):
    """Validate UTF-8 encoding"""
    i = 0
    n = len(data)

    while i < n:
        if data[i] < 128:
            i += 1
        else:
            try:
                bin_rep = to_bin(data[i])
                if bin_rep.startswith("110"):
                    assert to_bin(data[i+1]).startswith("10")
                    i += 2
                elif bin_rep.startswith("1110"):
                    assert to_bin(data[i+1]).startswith("10")
                    assert to_bin(data[i+2]).startswith("10")
                    i += 3
                elif bin_rep.startswith("11110"):
                    assert to_bin(data[i+1]).startswith("10")
                    assert to_bin(data[i+2]).startswith("10")
                    assert to_bin(data[i+3]).startswith("10")
                    i += 4
                else:
                    return False
            except (AssertionError, IndexError):
                return False

    return True
