#!/usr/bin/python3
"""
This module defines a solution to the making change problem.

See README.md.
"""


def makeChange(coins: list, total: int) -> int:
    """Return the fewest number of coins needed to meet a given total."""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin
    if total != 0:
        return -1
    return num_coins
