#!/usr/bin/python3
"""This file defines a solution to the Prime Game problem."""


def is_prime(n):
    """Return whether or not `n` is a prime number"""
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Return the winner of the game or None."""
    wins = []
    for round in range(x):
        n = nums[round]
        if n == 1:
            wins.append("Ben")
        else:
            primes = [i for i in range(1, n+1) if is_prime(i)]
            if len(primes) % 2:
                wins.append("Maria")
            else:
                wins.append("Ben")
    ben_wins, maria_wins = wins.count("Ben"), wins.count("Maria")
    if ben_wins > maria_wins:
        return "Ben"
    if maria_wins > ben_wins:
        return "Maria"
