"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""


def is_match(string, pattern):
    table = [[False] * (len(pattern) + 1) for _ in range(len(string) + 1)]
    table[0][0] = True

    for i, char in enumerate(pattern):
        if char == "*" and table[0][i - 1]:
            table[0][i + 1] = True

    for i, s_char in enumerate(string):
        for j, p_char in enumerate(pattern):
            if p_char == ".":
                table[i + 1][j + 1] = table[i][j]
            elif p_char == s_char:
                table[i + 1][j + 1] = table[i][j]
            elif p_char == "*":
                if pattern[j - 1] != string[i] and pattern[j - 1] != ".":
                    table[i + 1][j + 1] = table[i + 1][j - 1]
                else:
                    table[i + 1][j + 1] = table[i + 1][j] \
                        or table[i + 1][j - 1] \
                        or table[i][j + 1]

    return table[len(string)][len(pattern)]


def test():
    nums_list = [
        ("aa", "a"),
        ("aa", "aa"),
        ("aaa", "aa"),
        ("aa", "a."),
        ("aa", ".*"),
        ("ab", ".*"),
        ("aab", "c*a*b"),
        ("", ""),
        ("", ".*"),
        ("", "*")
    ]
    for (string, pattern) in nums_list:
        print(is_match(string, pattern))


test()
