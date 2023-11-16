#!/usr/bin/python3
"""
Problem:
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
  - Do this in-place
  - Assume the matrix will have 2 dimensions and will not be empty
"""
# from copy import deepcopy as dc
# import typing as t


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise in place."""
    size = len(matrix)
    copy = [row[:] for row in matrix]
    for row in range(size):
        for col in range(size - 1, -1, -1):
            matrix[row][-1 - col] = copy[col][row]
