"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7, a solution set is:
[
  [7],
  [2, 2, 3]
]
"""


def combination(nums, target):
    result = []
    nums.sort()
    backtrack(nums, target, result, [], 0)
    return result


def backtrack(nums, target, result, temp, start):
    if target == 0:
        result.append(temp[:])
    else:
        for i in range(start, len(nums)):
            if target < nums[i]:
                break
            temp.append(nums[i])
            backtrack(nums, target - nums[i], result, temp, start)
            temp.pop()
