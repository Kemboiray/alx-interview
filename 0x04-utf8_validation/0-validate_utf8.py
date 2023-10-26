#!/usr/bin/python3
"""This module defines the function `validUTF8`"""


# def validUTF8(data):
#     """Validate UTF-8 encoding for a data stream"""
#     count = 0
#     for num in data:
#         bin_rep = format(
#             num, '#010b')[-8:]  # Get the binary representation of the number
#         if count == 0:  # If this is the start of a new character
#             for bit in bin_rep:
#                 if bit == '0':
#                     break
#                 count += 1
#             if count == 0:
#                 continue
#             if count == 1 or count > 4:
#                 return False
#         else:
#             if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
#                 return False
#         count -= 1
#     return count == 0
def validUTF8(data):
    bin_reps = [format(d, '#010b').removeprefix('0b') for d in data]
    return all([
        len(b) == 8 and (b.startswith('0') or b.startswith('110')
                         or b.startswith('1110') or b.startswith('1111'))
        for b in bin_reps
    ])
