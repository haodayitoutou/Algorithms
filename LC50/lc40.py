"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, a solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


def combination(nums, target):
    nums.sort()
    result = []
    backtrack(nums, target, result, [], 0)
    return result


def backtrack(nums, target, result, temp, start):
    if target == 0:
        result.append(temp[:])
    else:
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if target < nums[i]:
                break
            temp.append(nums[i])
            backtrack(nums, target - nums[i], result, temp, i + 1)
            temp.pop()
