#!/usr/bin/python3
'''
Rotate 2D Matrix interview project
'''


def rotate_2d_matrix(matrix):
    '''
    Rotates an n x n 2D matrix 90 degrees clockwise in-place
    Args:
        param matrix: List of lists of integers representing the 2D matrix
    '''
    number = len(matrix)

    for i in range(number):
        for j in range(i, number):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(number):
        matrix[i].reverse()
