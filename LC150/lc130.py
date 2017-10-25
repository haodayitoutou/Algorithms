"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Do not return anything, modify board in-place instead.
"""


def dfs(board, row, col):
    board[row][col] = "*"

    nrow = len(board)
    ncol = len(board[0])
    if col > 1 and board[row][col - 1] == "O":
        dfs(board, row, col - 1)

    if col < ncol - 2 and board[row][col + 1] == "O":
        dfs(board, row, col + 1)

    if row > 1 and board[row - 1][col] == "O":
        dfs(board, row - 1, col)

    if row < nrow - 2 and board[row + 1][col] == "O":
        dfs(board, row + 1, col)


def find(board):
    if not board or not board[0]:
        return
    nrow = len(board)
    ncol = len(board[0])
    if nrow <= 2 or ncol <= 2:
        return
    for i in range(nrow):
        if board[i][0] == "O":
            dfs(board, i, 0)
        if board[i][ncol - 1] == "O":
            dfs(board, i, ncol - 1)

    for j in range(1, ncol - 1):
        if board[0][j] == "O":
            dfs(board, 0, j)
        if board[nrow - 1][j] == "O":
            dfs(board, nrow - 1, j)

    for i in range(nrow):
        for j in range(ncol):
            if board[i][j] == "O":
                board[i][j] = "X"
            if board[i][j] == "*":
                board[i][j] = "O"


def test():
    board_list = [
        [],
        [["X", "X", "O"],
         ["X", "O", "X"],
         ["O", "X", "X"]],
        [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]
    ]
    for board in board_list:
        find(board)
        print(board)


test()
