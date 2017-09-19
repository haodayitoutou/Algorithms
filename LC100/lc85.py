"""
Given a 2D binary matrix filled with 0's and 1's,
 find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
"""


def max_rectangle(matrix):
    result = 0
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return result

    n_col = len(matrix[0])
    n_row = len(matrix)
    height = [0 for _ in range(n_col + 1)]
    for row in range(n_row):
        for col in range(n_col):
            if matrix[row][col] == "1":
                height[col] += 1
            else:
                height[col] = 0

        stack = [0]
        for i in range(1, len(height)):
            while stack and height[i] < height[stack[-1]]:
                height1 = height[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                result = max(result, height1 * width)
            stack.append(i)
    return result


def test():
    matrix_list = [
        [""],
        ["10100", "10111", "11111", "10010"],
        ["110101", "010011", "111101", "111101"]
    ]

    for matrix in matrix_list:
        print(max_rectangle(matrix))


test()
