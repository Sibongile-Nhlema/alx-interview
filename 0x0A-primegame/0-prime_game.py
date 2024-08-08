#!/usr/bin/python3
'''
This module helps find out who wins a game
where you remove prime numbers and their multiples
from a list of numbers.
'''
#!/usr/bin/python3
'''
Module that handles the determining the winner of a game
based on the strategic removal of prime numbers and their
multiples from a set of consecutive integers.
'''


def sieve_of_eratosthenes(max_n):
    '''
    Generates prime numbers up to max_n
    using the Sieve of Eratosthenes
    '''
    sieve = [True] * (max_n + 1)
    sieve[0], sieve[1] = False, False

    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    primes = [i for i in range(2, max_n + 1) if sieve[i]]

    return primes, sieve


def count_prime_multiples(sieve, n):
    '''
    Counts how many primes and their multiples
    can be removed from the set 1 to n
    '''
    count = 0
    for i in range(2, n + 1):
        if sieve[i]:
            count += 1
            for j in range(i, n + 1, i):
                sieve[j] = False

    return count


def isWinner(x, nums):
    '''
    Determines the winner of the game
    '''
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes, sieve = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        sieve_copy = sieve[:n + 1]
        prime_count = count_prime_multiples(sieve_copy, n)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None