"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


def permutation(nums):
    result = []
    backtrack(nums, result, [])
    return result


def backtrack(nums, result, temp):
    if len(temp) == len(nums):
        result.append(temp[:])
        return
    for number in nums:
        if number in temp:
            continue
        temp.append(number)
        backtrack(nums, result, temp)
        temp.pop()
