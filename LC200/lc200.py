"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3
"""


def num_islands(grid):
    if not grid or not grid[0]:
        return 0
    nrow = len(grid)
    ncol = len(grid[0])
    total = 0
    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] == "1":
                total += 1
                mark(grid, i, j)

    return total


def mark(grid, row, col):
    nrow = len(grid)
    ncol = len(grid[0])
    if row < 0 or row >= nrow or col < 0 or col >= ncol:
        return
    if grid[row][col] == "1":
        grid[row][col] = "X"

        mark(grid, row - 1, col)
        mark(grid, row + 1, col)
        mark(grid, row, col - 1)
        mark(grid, row, col + 1)


def test():
    grid1 = [["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]
    print(num_islands(grid1))

    grid2 = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]
    print(num_islands(grid2))

    grid3 = []
    print(num_islands(grid3))


test()
