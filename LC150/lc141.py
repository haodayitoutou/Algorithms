"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


def cycle(head):
    if head is None:
        return False
    pt1 = head
    pt2 = head
    while pt2.next and pt2.next.next:
        pt1 = pt1.next
        pt2 = pt2.next
        if pt1 is pt2:
            return True
    return False
