"""
Given n non-negative integers a1, a2, ..., an,
 where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that
 the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
 such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


def max_container(nums):
    i = 0
    j = len(nums) - 1
    max_volumn = 0
    while i < j:
        height = min(nums[i], nums[j])
        volumn = height * (j - i)
        if volumn > max_volumn:
            max_volumn = volumn

        if nums[i] < nums[j]:
            while i < j and nums[i] <= height:
                i += 1
        else:
            while i < j and nums[j] <= height:
                j -= 1

    return max_volumn


def test():
    nums_list = [
        [1, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 11, 2, 12, 3, 3, 16],
        [1, 11, 2, 12, 3, 6]
    ]

    for nums in nums_list:
        print(max_container(nums))


test()
