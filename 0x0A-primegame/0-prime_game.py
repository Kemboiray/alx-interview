#!/usr/bin/python3
"""This file defines a solution to the Prime Game problem."""


def is_prime(n: int) -> bool:
    """Return whether or not `n` is a prime number"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x: int, nums: list):
    """Return the winner of the game or None."""
    tally = {}
    for round in nums:
        set = list(range(1, round + 1))
        primes = [i for i in set if is_prime(i)]
        last_success = "Ben"
        for n in primes:
            if n in set:
                fact = n
                while fact <= max(set):
                    set.remove(fact)
                    fact += n
                last_success = "Ben" if primes.index(n) % 2 else "Maria"
        tally[round] = last_success

    maria_wins = len([val for val in tally.values() if val == "Maria"])
    ben_wins = len([val for val in tally.values() if val == "Ben"])
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
