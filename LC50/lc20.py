"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

The brackets must close in the correct order,
 "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


def is_valid(parenthese):
    stack = []
    pairs = {
        "]": "[",
        "}": "{",
        ")": "("
    }

    for char in parenthese:
        if char in pairs:
            other_half = pairs[char]
            if not stack or stack[-1] != other_half:
                return False
            stack.pop()
        else:
            stack.append(char)

    return stack == []


def test():
    strings = [
        "[",
        "]",
        "[]",
        "][",
        "([{{}}])",
        "([{]})"
    ]

    for a_string in strings:
        print(is_valid(a_string))


test()
