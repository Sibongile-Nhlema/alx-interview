#!/usr/bin/python3
'''
Module that helps determine the winner of a game
where you remove prime numbers and their multiples
from a list of numbers.
'''

def sieve_of_eratosthenes(max_n):
    '''
    Generates prime numbers up to max_n
    using the Sieve of Eratosthenes.
    '''
    sieve = [True] * (max_n + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes

    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    primes = [i for i in range(2, max_n + 1) if sieve[i]]
    return sieve


def isWinner(x, nums):
    '''
    Determines the winner of the game.
    '''
    if not nums or x < 1:
        return None

    max_n = max(nums)
    sieve = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue
        
        count = 0
        sieve_copy = sieve[:n + 1]
        
        for i in range(2, n + 1):
            if sieve_copy[i]:
                count += 1
                for j in range(i, n + 1, i):
                    sieve_copy[j] = False
        
        if count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

