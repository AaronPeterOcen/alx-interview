#!/usr/bin/python3
"""
Defines a make change function that returns fewest number of coins needed to meet total
"""


def makeChange(coins, total):
    """
    Minimum coins required
    """
    if total <= 0:
        return 0
    trace, count = 0, 0
    coins.sort()
    coins = coins[::-1]
    while len(coins) > 0:
        value = coins[0]:
        if trace + value > total:
            coins.pop(0)
            continue
        trace += value
        count += 1
        if trace == total:
            return count
    return -1
