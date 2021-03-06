"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""


def is_palindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if not string[left].isalnum():
            left += 1
        elif not string[right].isalnum():
            right -= 1
        else:
            if string[left].lower() != string[right].lower():
                return False
            left += 1
            right -= 1
    return True
