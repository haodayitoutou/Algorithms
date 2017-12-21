"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


def find(haystack, needle):
    i = 0
    while True:
        j = 0
        while True:
            if j == len(needle):
                return i
            if i + j == len(haystack):
                return -1
            if needle[j] != haystack[i]:
                break
            j += 1
        i += 1
