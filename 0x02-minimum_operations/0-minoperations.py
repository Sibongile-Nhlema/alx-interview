#!/usr/bin/python3
'''
Module handles the implementation of min operations
There can only be either a cpoy or paste operation
'''


def minOperations(n):
    '''
    Calculates the min operation needed for h = n
    Args:
        n (int): ninterger given
    Returns:
        interger: indicates the min operations needed
    The result must be the sum of the factors and their powers
    '''
    number_of_operations = 0
    if (n <= 0):
        return 0

    divisor = 2
    while (n > 1):
        while (n % divisor == 0):
            number_of_operations += divisor
            n //= divisor
        divisor

    return number_of_operations
