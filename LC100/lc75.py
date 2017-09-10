"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2
to represent the color red, white, and blue respectively.
"""


def sort_color(nums):
    less = 0
    i = 0
    greater = len(nums) - 1
    while i <= greater:
        if nums[i] == 0:
            nums[less], nums[i] = nums[i], nums[less]
            i += 1
            less += 1
        elif nums[i] == 1:
            i += 1
        else:  # nums[i] == 2
            nums[greater], nums[i] = nums[i], nums[greater]
            greater -= 1
