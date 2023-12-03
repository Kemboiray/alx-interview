#!/usr/bin/python3
"""Solution to island perimeter problem."""


def island_perimeter(grid):
    """Return the perimeter of an island described by ``grid``"""

    def neighbours(i, j):
        """
        Return the number of neighbours bordering the element ``grid[i][j]``
        """
        return sum(
            [grid[i - 1][j], grid[i][j - 1], grid[i + 1][j], grid[i][j + 1]])

    i, perimeter = 1, 0
    while i < len(grid):
        j = 1
        while j < len(grid[i]):
            # print(f"Iteration: grid[{i}][{j}]")
            if grid[i][j] == 1:
                perimeter += 4 - neighbours(i, j)
            j += 1
        i += 1

    return perimeter
