#!/usr/bin/python3
"""Solution to island perimeter problem."""


def island_perimeter(grid):
    """Return the perimeter of an island described by ``grid``"""

    def neighbours(i, j):
        """
        Return the number of neighbours bordering the element ``grid[i][j]``
        """
        if i == 0:
            up = 0
        else:
            up = grid[i - 1][j]
        if i == len(grid) - 1:
            down = 0
        else:
            down = grid[i + 1][j]
        if j == 0:
            left = 0
        else:
            left = grid[i][j - 1]
        if j == len(grid[i]) - 1:
            right = 0
        else:
            right = grid[i][j + 1]
        return sum([up, down, left, right])

    i, perimeter = 0, 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            # print(f"Iteration: grid[{i}][{j}]")
            if grid[i][j] == 1:
                perimeter += 4 - neighbours(i, j)
            j += 1
        i += 1

    return perimeter
