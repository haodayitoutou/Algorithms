"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
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
        if i > lower and nums[i] == nums[i - 1]:
            continue
        temp.append(nums[i])
        subset_help(result, temp, nums, i + 1)
        temp.pop()
