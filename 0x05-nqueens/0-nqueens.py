#!/usr/bin/python3
"""Thes module defines a solution to the `N-queens` problem"""

import sys


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


def main():
    """Begin program execution"""
    n = validate()
    if n == 1:
        sys.exit(1)
    pass


if __name__ == "__main__":
    main()
