"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays.
 The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


def find_median(nums1, nums2):
    if len(nums1) > len(nums2):  # make sure length 1 <= length2
        nums1, nums2 = nums2, nums1

    length1, length2 = len(nums1), len(nums2)
    imin, imax = 0, length1

    if length2 == 0:
        return "Invalid input"

    while imin <= imax:
        i = (imin + imax) // 2

        # i + j = (length1 - i + length2 - j)          Even
        #      or (length1 - i + length2 - j + 1)      Odd
        # i + j = (length1 + length2) / 2 or (length1 + length2 + 1) / 2
        # i + j = (length1 + length2 + 1) // 2
        j = (length1 + length2 + 1) // 2 - i

        if i > 0 and nums1[i - 1] > nums2[j]:
            # i>0 ==> j = (l1 + l2 + 1) // 2 - i < (l1 + l2 + 1) // 2
            # l1 <= l2 ==> j < (2*l2 + 1) // 2
            # so, i > 0 ==> j < length2
            imax = i - 1  # find a smaller i
        elif i < length1 and nums2[j - 1] > nums1[i]:
            # i<l1 ==> j = (l1 + l2 + 1) // 2 - i > (l1 + l2 + 1) // 2 - l1
            #            > (l2 - l1 + 1) // 2
            # l1 <= l2 ==> j > 0
            # so, i < length1 ==> j > 0
            imin = i + 1  # find a greater i
        else:
            if i == 0:
                left_max = nums2[j - 1]
            elif j == 0:
                left_max = nums1[i - 1]
            else:
                left_max = max(nums1[i - 1], nums2[j - 1])

            if (length1 + length2) % 2 == 1:
                return left_max

            if i == length1:
                right_min = nums2[j]
            elif j == length2:
                right_min = nums1[i]
            else:
                right_min = min(nums1[i], nums2[j])

            return (left_max + right_min) / 2.0


def test():
    n1_list = [
        [],
        [],
        [1, 2],
        [3, 4],
        [1, 4, 12, 51],
        [1, 4, 12, 32, 44],
        [1, 4, 12, 21, 32, 44],
        [1, 1, 1]
    ]
    n2_list = [
        [],
        [1],
        [3, 4],
        [1, 2, 3],
        [2],
        [15, 24, 34, 47, 65, 66],
        [15, 24, 34, 47, 65, 66],
        [2, 2, 2]
    ]

    for nums1, nums2 in zip(n1_list, n2_list):
        median = find_median(nums1, nums2)

        print(nums1, nums2, median)
        print("\n")


test()
