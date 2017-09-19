"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_numbers(number1, number2):
    output = ListNode(0)
    first = output
    plus_one = False
    while number1 or number2:
        new_val = 0
        if number1:
            new_val += number1.val
            number1 = number1.next
        if number2:
            new_val += number2.val
            number2 = number2.next

        if plus_one:
            new_val += 1

        if new_val >= 10:
            new_val -= 10
            plus_one = True
        else:
            plus_one = False

        new_node = ListNode(new_val)
        first.next = new_node
        first = new_node

    if plus_one:
        first.next = ListNode(1)
    return output.next
