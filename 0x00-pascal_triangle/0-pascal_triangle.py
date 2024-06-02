#!/usr/bin/python3
'''
This module handles the implementation of pascal's triangle
Using the Pascal's Triagnle Formula directly
'''


def pascal_triangle(n):
    '''
    Implements the pascal's triangle function
    Args:
        n: interger
    Return: returns a list of intergers representin the tiangles of pascal of n
    '''
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for row in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        next_row = [1]  # Start the new row with 1

        # Fill in the middle values, where m is the value
        for m in range(1, len(prev_row)):
            # formula = nCm = n-1Cm-1 + n-1Cm
            next_row.append(prev_row[m-1] + prev_row[m])

        next_row.append(1)  # End the next row with 1
        triangle.append(next_row)  # Add the next row to the triangle

    return triangle
