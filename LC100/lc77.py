"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


def combinations(number, k):
    result = []
    combinations_help(result, [], number, k, 0)
    return result


def combinations_help(result, temp, number, k, lower):
    if k == 0:
        result.append(temp[:])
        return
    for i in range(lower + 1, number - k + 2):
        temp.append(i)
        combinations_help(result, temp, number, k - 1, i)
        temp.pop()
