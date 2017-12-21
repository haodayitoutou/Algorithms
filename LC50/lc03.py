"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def longest(string):
    start, maximum = 0, 0
    used = {}
    for i, char in enumerate(string):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            maximum = max(maximum, i - start + 1)
        used[char] = i
    return maximum
