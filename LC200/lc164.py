"""
Given an unsorted array, find the maximum difference
 between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers
 and fit in the 32-bit signed integer range.
"""

import math


def maximum_cap(nums):
    if len(nums) < 2:
        return 0

    length = len(nums)
    minimum = min(nums)
    maximum = max(nums)
    if minimum == maximum:
        return 0

    gap = int(math.ceil(float(maximum - minimum) / (length - 1)))
    num_buckets = int(math.ceil(float(maximum - minimum) / gap))
    bucket_min = [None] * num_buckets
    bucket_max = [None] * num_buckets

    for number in nums:
        if number == minimum or number == maximum:
            continue

        index = (number - minimum) // gap  # integer = integer / integer
        cur_min, cur_max = bucket_min[index], bucket_max[index]
        if cur_min is None:
            bucket_min[index] = number
            bucket_max[index] = number
        else:
            bucket_min[index] = min(number, cur_min)
            bucket_max[index] = max(number, cur_max)

    max_cap = 0
    previous_max = minimum
    for i in range(num_buckets):
        if bucket_min[i] is None:
            continue
        max_cap = max(max_cap, bucket_min[i] - previous_max)
        previous_max = bucket_max[i]

    return max(max_cap, maximum - previous_max)


def test():
    nums_list = [
        [],
        [1, 1],
        [10, 21, 17, 13, 22, 23, 28, 30],
        [1, 1, 1, 1, 5, 5, 5, 5],
        [41, 42, 81],
        [2, 6]
    ]

    for nums in nums_list:
        print(maximum_cap(nums))


test()
