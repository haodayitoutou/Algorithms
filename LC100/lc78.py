"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


def subset(nums):
    result = []
    nums.sort()
    subset_help(result, [], nums, 0)
    return result


def subset_help(result, temp, nums, lower):
    result.append(temp[:])
    for i in range(lower, len(nums)):
        temp.append(nums[i])
        subset_help(result, temp, nums, i + 1)
        temp.pop()
