"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]
"""


def search_range(nums, target):
    if not nums:
        return [-1, -1]
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    if nums[low] != target:
        return [-1, -1]
    start = low

    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    if nums[low] != target:
        low -= 1

    return [start, low]


def test():
    nums_list = [
        [],
        [2, 3],
        [11, 12],
        [8],
        [8, 8],
        [8, 8, 8],
        [7, 8, 9],
        [4, 5, 7, 8, 8, 9, 10],
        [5, 6, 8, 8],
        [8, 8, 9, 10],
        [1, 3, 5, 6, 7, 8]
    ]
    for nums in nums_list:
        print(search_range(nums, 8))


test()
