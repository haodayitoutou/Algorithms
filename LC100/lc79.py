"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


def exist(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, i, j):
                return True
    return False


def dfs(board, word, i, j):
    if not word:
        return True
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j]:
        return False
    temp = board[i][j]
    board[i][j] = "#"
    result = dfs(board, word[1:], i - 1, j) or \
        dfs(board, word[1:], i + 1, j) or \
        dfs(board, word[1:], i, j - 1) or \
        dfs(board, word[1:], i, j + 1)
    board[i][j] = temp
    return result
