#!/usr/bin/python3


def island_perimeter(grid):
    """
        a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100`
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 4 * sum(sum(row) for row in grid)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter -= 2 * (
                    (row > 0 and grid[row - 1][col] == 1)
                    + (col > 0 and grid[row][col - 1] == 1)
                )
    return perimeter
