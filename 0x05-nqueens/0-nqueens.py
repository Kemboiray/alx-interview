#!/usr/bin/python3
"""Thes module defines a solution to the `N-queens` problem"""

import sys
from typing import List


def validate():
    """Validate correct inpot"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        return 1
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        return 1
    if n < 4:
        print("N must be at least 4")
        return 1
    return n


def nqueens(n: int) -> List:
    """Generate a solution to `N-queens` puzzle"""
    board, used_columns, i = [], set(), 0
    for j in range(n):
        if j not in used_columns:
            board.append([i, j])
            i += 1
        used_columns.add(j)
    print(used_columns)
    return board


def main():
    """Begin program execution"""
    n = validate()
    if n == 1:
        sys.exit(1)
    print(nqueens(n))


if __name__ == "__main__":
    main()
