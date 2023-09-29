#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module defines a function that creates a Pascal triangle."""


def pascal_triangle(n: int) -> list:
    """Return a pascal triangle"""
    triangle = [[] for _ in range(n)]
    i = 0
    while i < n:
        j = 0
        while j <= i:
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
            j += 1
        i += 1
    return triangle
