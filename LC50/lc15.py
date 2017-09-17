"""
Given an array S of n integers, are there elements a, b, c in S
 such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def three_sum(nums):
    output = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i != 0 and nums[i] == nums[i - 1]:
            continue

        first = nums[i]
        target = -first

        j = i + 1
        k = len(nums) - 1
        while j < k:
            second = nums[j]
            third = nums[k]

            if second + third == target:
                output.append([first, second, third])
                j += 1
                while j < k and nums[j + 1] == second:
                    j += 1

                k -= 1
                while j < k and nums[k - 1] == third:
                    k -= 1
            elif second + third < target:
                j += 1
            else:
                k -= 1

    return output


def test():
    nums_list = [
        [0, 0, 0],
        [-1, 0, 1, 2, -1, -4]
    ]
    for nums in nums_list:
        print(nums)
        print(three_sum(nums))
        print("\n")


test()
