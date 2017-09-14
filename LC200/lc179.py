"""
Given a list of non negative integers,
 arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large,
 so you need to return a string instead of an integer.
"""


def largest_number(nums):
    if not nums:
        return ""
    nums = [str(n) for n in nums]

    def compare(string1, string2):
        number1 = int(string1 + string2)
        number2 = int(string2 + string1)

        return number2 - number1

    def cmp_to_key(mycmp):
        class Key:
            def __init__(self, obj):
                self.obj = obj

            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0

            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
        return Key

    nums.sort(key=cmp_to_key(compare))
    if nums[0] == "0":
        return "0"
    return "".join(nums)


def test():
    nums_list = [
        [],
        [1],
        [0, 0],
        [3, 30, 34, 5, 9, 0],
        [1, 0, 0],
        [21, 12, 23, 32]
    ]

    for nums in nums_list:
        print(largest_number(nums))


test()
