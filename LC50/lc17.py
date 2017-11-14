"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


def combinations(digits):
    if not digits:
        return []
    result = [""]
    mappings = {"1": "*",
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
                "0": " "}
    for i, char in enumerate(digits):
        while len(result[0]) == i:
            prev = result.pop(0)
            for new in mappings[char]:
                result.append(prev + new)
    return result


def test():
    digit_list = [
        "",
        "1",
        "2",
        "13",
        "23",
        "043"
    ]
    for digit in digit_list:
        print(combinations(digit))


test()
