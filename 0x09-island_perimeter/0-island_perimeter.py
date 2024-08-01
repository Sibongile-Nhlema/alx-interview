#!/usr/bin/python3
'''Module for calculating the perimeter of a single island in a grid,
where the grid is represented by a 2D array of integers
'''


def island_perimeter(grid):
    '''
    Calculate the perimeter of the island in the grid.
    Args:
    grid (list of list of int): A 2D grid representing the
    map where 0 is water and 1 is land.
    Returns:
    int: The perimeter of the island.
    '''
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0

    for row_idx in range(rows):
        for col_idx in range(columns):
            if grid[row_idx][col_idx] == 1:
                # Check top
                if row_idx == 0 or grid[row_idx - 1][col_idx] == 0:
                    perimeter += 1
                # Check bottom
                if row_idx == rows - 1 or grid[row_idx + 1][col_idx] == 0:
                    perimeter += 1
                # Check left
                if col_idx == 0 or grid[row_idx][col_idx - 1] == 0:
                    perimeter += 1
                # Check right
                if col_idx == columns - 1 or grid[row_idx][col_idx + 1] == 0:
                    perimeter += 1

    return perimeter
