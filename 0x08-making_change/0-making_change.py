#!/usr/bin/python3
'''
Module for the making change problem
'''


def makeChange(coins, total):
    '''
    Determines the fewest number of coins needed
    to meet a given amount total.
    Args:
        coins (list): List of coin values.
        total (int): total amount given.
    Returns:
        int: Fewest number of coins needed to meet
        the total, or -1 if it cannot be met.
    '''
    if total <= 0:
        return 0

    # Initialize the min_coins list with infinity value (highest)
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            min_coins[amount] = min(min_coins[amount],
                                    min_coins[amount - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
