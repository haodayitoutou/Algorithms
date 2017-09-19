"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""


def remove(head, count):
    previous = head
    end = head
    for _ in range(count):
        end = end.next
    if not end:
        return head.next

    while end.next:
        previous = previous.next
        end = end.next
    previous.next = previous.next.next
    return head
