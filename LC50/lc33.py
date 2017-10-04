"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


def find(nums, target):
    if not nums:
        return -1
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if target >= nums[low] and target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if target <= nums[high] and target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
    if nums[low] == target:
        return low
    return -1


def test():
    nums1 = [11, 13, 15, 17, 2, 4, 6]
    nums2 = [11, 13, 15, 17, 2, 4, 6, 8]
    target_list = [
        1, 3, 4, 6, 8, 10, 11, 12, 15, 16, 20
    ]
    for target in target_list:
        print("Target is {}, index1 = {}, index2 = {}".format(
            target,
            find(nums1, target),
            find(nums2, target)
        ))


test()
