#!/usr/bin/python3
"""
This module defines the function `minOperations`, which returns the sum of a
number's prime factors. This solves the problem of computing the fewest
operations needed to result in `n` characters in a file given an initial
condition of one character and a text editor that can only either copy all text
or paste into the buffer.
"""


def minOperations(n: int) -> int:
    """Return the sum of `n`'s prime factors"""
    factors = [0]
    i = 2
    while i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    return sum(factors)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} n")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("n must be a number")
        exit(1)
    print(minOperations(n))
