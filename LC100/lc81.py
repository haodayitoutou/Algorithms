"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
"""


def search(nums, target):
    if not nums:
        return False
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > nums[low]:
            if target >= nums[low] and nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[mid] < nums[low]:
            if target < nums[low] and nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            low += 1
    return nums[low] == target


def test():
    file = open("test.txt", 'w')
    nums1 = [9, 11, 13, 15, 21, 24, 3, 5, 7]
    nums2 = [8, 8, 8, 8, 13, 5, 7, 8]
    nums3 = [8, 19, 24, 6, 8, 8, 8, 8]

    for target1 in [1, 3, 4, 5, 7, 8, 12, 14, 20, 22, 24, 26]:
        file.write("{} - {} - {}\n".format(nums1,
                                           target1,
                                           search(nums1, target1)))
    file.write("\n")

    for target2 in [3, 5, 6, 7, 8, 9, 11, 13, 14, 15]:
        file.write("{} - {} - {}\n".format(nums2,
                                           target2,
                                           search(nums2, target2)))
    file.write("\n")

    for target3 in [3, 5, 7, 8, 9, 12, 19, 20, 22, 23, 24, 26]:
        file.write("{} - {} - {}\n".format(nums3,
                                           target3,
                                           search(nums3, target3)))

    file.close()


test()
