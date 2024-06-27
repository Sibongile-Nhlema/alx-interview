#!/usr/bin/python3
'''
Module for the implementation of the validUTF6 method
'''


def validUTF8(data):
    '''
    method that determines if a given data set
    represents a valid UTF-8 encoding
    Args:
        data (set): given data set
    Returns:
        Boolean: true is is valid, otherwise false

    Prep:
    - (1 << 7): Shifts 1 to the left by 7 positions, resulting in 0b10000000.
    - (1 << 6 | 1 << 5): Shifts 1 to the left by 6 positions,
    OR shifts 1 to the left by 5 positions,
    resulting in 0b11100000.
    - (1 << 5): Shifts 1 to the left by 5 positions, resulting in 0b11000000.
    - (1 << 4): Shifts 1 to the left by 4 positions, resulting in 0b10000.
    '''
    start_mask = [0b10000000, 0b11100000, 0b11110000, 0b11111000]
    # Number of bytes each UTF-8 character can occupy
    num_of_bytes = [1, 2, 3, 4]

    # Iterate through the given data set
    i = 0
    while i < len(data):
        # Find the num_of_bytes for current character

        # Check first byte to find the num_of_bytes in the sequence

        # equals 0b10000000
        if data[i] >= (1 << 7):
            return False

        # equals 0b11100000
        elif data[i] >= (1 << 6 | 1 << 5):
            nbytes = 3

        # equals 0b11000000
        elif data[i] >= (1 << 5):
            nbytes = 2

        # equals 0b10000000
        elif data[i] >= (1 << 4):
            nbytes = 1

        else:
            return False

        # Check if there are enough bytes left in data
        if i + nbytes > len(data):
            return False

        # Validate the sequence
        for j in range(1, nbytes):
            if (data[i + j] & (1 << 7) | (1 << 6)) != (1 << 7):
                return False

        # Move to the next character
        i += nbytes

    return True
