"""
Given n non-negative integers representing an elevation map
 where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example, given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""


def trap(nums):
    total = 0
    left = 0
    right = len(nums) - 1
    max_l = 0
    max_r = 0
    while left < right:
        if nums[left] <= nums[right]:
            if nums[left] >= max_l:
                max_l = nums[left]
            else:
                total += (max_l - nums[left])
            left += 1
        else:
            if nums[right] >= max_r:
                max_r = nums[right]
            else:
                total += (max_r - nums[right])
            right -= 1
    return total


def test():
    nums_list = [
        [0, 0, 0],
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 2]
    ]
    for nums in nums_list:
        print("{} --> {}".format(nums, trap(nums)))


test()
