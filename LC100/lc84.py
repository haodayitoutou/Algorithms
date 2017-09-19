"""
Given n non-negative integers representing the histogram's bar height
 where the width of each bar is 1,
 find the area of largest rectangle in the histogram.

For example,
Given heights = [2,1,5,6,2,3],
return 10
"""


def largest(nums):
    """
    Calculate area for each bar as if it is the smallest one
     among the rectangle.
    """
    result = 0
    stack = [0]
    nums.append(0)

    for i in range(1, len(nums)):
        while stack and nums[i] < nums[stack[-1]]:
            height = nums[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            result = max(result, height * width)

        stack.append(i)

    return result


def test():
    nums_list = [
        [],
        [2, 1, 5, 6, 2, 3],
        [1, 1],
        [5, 1, 5],
        [1, 5, 1],
        [1, 2, 3, 4, 5],
        [4, 5, 6, 3, 6, 7, 8, 2]
    ]

    for nums in nums_list:
        print(largest(nums))


test()
