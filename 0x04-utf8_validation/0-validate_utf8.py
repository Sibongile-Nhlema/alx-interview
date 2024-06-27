#!/usr/bin/python3
'''
Module for the implementation of the validUTF6 method
'''


def validUTF8(data):
    '''
    Method that determines if a given data set
    represents a valid UTF-8 encoding.
    Args:
        data (list): Given data set represented by a list of integers.
    Returns:
        bool: True if data is a valid UTF-8 encoding, otherwise False.
    '''
    start_mask = [0b10000000, 0b11100000, 0b11110000, 0b11111000]
    continuation_mask = 0b11000000
    # Number of bytes each UTF-8 character can occupy
    num_of_bytes = [1, 2, 3, 4]

    # Iterate through the given data set
    i = 0
    while i < len(data):
        # Find the number of bytes for current character

        # Check the first byte to determine the number of bytes in the sequence

        if data[i] >= 0b11111000:
            # 5-byte and larger sequences - invalid in UTF-8
            return False
        elif data[i] >= 0b11110000:
            # 4-byte sequence - valid
            nbytes = 4
        elif data[i] >= 0b11100000:
            # 3-byte sequence - valid
            nbytes = 3
        elif data[i] >= 0b11000000:
            # 2-byte sequence - valid
            nbytes = 2
        else:
            # 1-byte sequence - valid
            nbytes = 1

        # Check if there are enough bytes left in data
        if i + nbytes > len(data):
            return False

        # Validate the sequence
        for j in range(1, nbytes):
            if (data[i + j] & 0b11000000) != 0b10000000:
                return False

        # Move to the next character
        i += nbytes

    return True
