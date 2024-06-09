#!/usr/bin/python3
'''
This module handles the implementation of lockboxes.
It includes a function that checks whether all boxes
can be unlocked.
'''


def canUnlockAll(boxes):
    '''
    Checks/decides whether all the boxes can be opened.
    Args:
        boxes (list of list of int): A list of lists where
        each sublist contains keys to other boxes.
        The first box boxes[0] is always unlocked.
    Returns:
        bool: True if all boxes can be opened, otherwise False.
    '''
    if not boxes:
        return False

    n = len(boxes)
    opened = [False] * n  # Initialize a list to keep track of opened boxes
    opened[0] = True  # The first box is always open
    queue = [0]

    while queue:
        # Get the first box from the queue
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                # Add the box to the queue to explore its keys
                queue.append(key)

    return all(opened)
