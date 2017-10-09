"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""


def search(matrix, target):
    if not matrix:
        return False
    row_count = len(matrix)
    col_count = len(matrix[0])
    low = 0
    high = row_count * col_count - 1
    while low <= high:
        mid = low + (high - low) // 2
        row = mid // col_count
        col = mid % col_count
        value = matrix[row][col]
        if value == target:
            return True
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def test():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target_list = [
        0, 1, 2, 3, 4, 7, 10, 15, 16, 20, 23, 30, 36, 50, 51
    ]
    for target in target_list:
        print("{} - {}".format(target, search(matrix, target)))


test()
