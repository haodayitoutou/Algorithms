"""
Given an array of integers,
 return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum(nums, target):
    note = {}
    for i, number in enumerate(nums):
        if number in note:
            j = note[number]
            if i < j:
                return [i, j]
            return [j, i]
        else:
            counter = target - number
            note[counter] = i


def test():
    nums_list = [
        [3, 2, 4],
        [2, 11, 53, 7],
        [1, 3, 4, 5, 42, 16, 17, 12]
    ]
    target_list = [
        6, 9, 16
    ]

    for nums, target in zip(nums_list, target_list):
        print(two_sum(nums, target))


test()
