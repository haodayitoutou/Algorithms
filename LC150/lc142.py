"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
"""


def cycle(head):
    if head is None or head.next is None:
        return None
    pt1 = head
    pt2 = head
    while True:
        if pt2.next is None or pt2.next.next is None:
            return None
        pt1 = pt1.next
        pt2 = pt2.next.next
        if pt1 is pt2:
            break

    pt3 = head
    while pt2 is not pt3:
        pt2 = pt2.next
        pt3 = pt3.next
    return pt2
