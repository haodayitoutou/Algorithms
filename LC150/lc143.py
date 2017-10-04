"""
Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
from util import create_node_list, print_node_list


def reorder(head):
    if head is None:
        return head

    pt1 = head
    pt2 = head
    while pt2.next and pt2.next.next:
        pt1 = pt1.next
        pt2 = pt2.next.next

    tail = None
    curr = pt1.next
    while curr:
        temp = curr.next
        curr.next = tail
        tail = curr
        curr = temp
    pt1.next = tail

    pt0 = head
    while pt0 is not pt1:
        temp = pt1.next
        pt1.next = temp.next
        temp.next = pt0.next
        pt0.next = temp

        pt0 = temp.next

    return head


def test():
    nums_list = [
        [],
        [1],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6]
    ]
    for nums in nums_list:
        head = create_node_list(nums)
        print_node_list(reorder(head))


test()
