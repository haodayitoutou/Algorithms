"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1: 123 -- 321
Example 2: -123 -- -321
Example 3: 120 -- 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


def reverse(integer):
    positivity = integer / abs(integer) if integer != 0 else 0
    rev = int(str(positivity * integer)[::-1])
    return positivity * rev * (integer < 2**31)
