#!/usr/bin/python3
"""This module defines the function `validUTF8`"""


def validUTF8(data):
    """Validate UTF-8 encoding for a data stream"""
    bin_reps = [format(d, '#010b')[2:] for d in data]
    return all([
        len(b) == 8 and (b.startswith('0') or b.startswith('110')
                         or b.startswith('1110') or b.startswith('1111'))
        for b in bin_reps
    ])
