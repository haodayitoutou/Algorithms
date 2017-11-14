"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def permutation(nums):
    nums.sort()
    result = []
    used = [False] * len(nums)
    backtrack(nums, used, result, [])
    return result


def backtrack(nums, used, result, temp):
    if len(nums) == len(temp):
        result.append(temp[:])
        return

    for i, number in enumerate(nums):
        if used[i]:
            continue
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue
        used[i] = True
        temp.append(number)
        backtrack(nums, used, result, temp)
        temp.pop()
        used[i] = False


def test():
    print(permutation([1, 1, 2]))


test()
