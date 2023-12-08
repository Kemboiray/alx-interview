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
    tally = {}
    for round in nums:
        if round == 1:
            tally[round] = "Ben"
        else:
            collection = list(range(1, round + 1))
            primes = [i for i in collection if is_prime(i)]
            for n in primes:
                if n in collection:
                    fact = n
                    last = max(collection)
                    while fact <= last:
                        if fact in collection:
                            collection.remove(fact)
                        fact += n
                    last_success = "Ben" if primes.index(n) % 2 else "Maria"
            tally[round] = last_success

    maria_wins = len([val for val in tally.values() if val == "Maria"])
    ben_wins = len([val for val in tally.values() if val == "Ben"])

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
