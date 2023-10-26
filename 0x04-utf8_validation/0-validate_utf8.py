#!/usr/bin/python3
"""This module defines the function `validUTF8`"""


def validUTF8(data):
    """Validate UTF-8 encoding for a data stream"""
    return all([i < 247 for i in data])
