#!/usr/bin/python3
"""This file defines a solution to the Prime Game problem."""


def is_prime(n):
    """Return whether or not `n` is a prime number"""
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Return the winner of the game or None."""
    ben, maria = 0, 0
    for round in range(x):
        n = nums[round]
        if n == 0:
            maria += 1
        elif n == 1:
            ben += 1
        else:
            primes = [i for i in range(1, n+1) if is_prime(i)]
            if len(primes) % 2:
                maria += 1
            else:
                ben += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
