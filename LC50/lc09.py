"""
Determine whether an integer is a palindrome. Do this without extra space.
"""


def is_palindrome(number):
    if number < 0:
        return False
    if number != 0 and number % 10 == 0:
        return False
    revert = 0
    while revert < number:
        revert = revert * 10 + number % 10
        number = number // 10
    return (number == revert or number == revert // 10)
