"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
from util import create_node_list, print_node_list


def rotate(head, k):
    if head is None or head.next is None or k == 0:
        return head
    pt1 = head
    length = 1
    while pt1.next:
        pt1 = pt1.next
        length += 1

    k = k % length
    if k == 0:
        return head

    pt2 = head
    for _ in range(length - k - 1):
        pt2 = pt2.next

    new_head = pt2.next
    pt2.next = None
    pt1.next = head
    return new_head


def test():
    nums_list = [
        [],
        [1],
        [1, 2],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4, 5]
    ]
    k_list = [
        0, 1, 1, 2, 10, 2
    ]
    for nums, k in zip(nums_list, k_list):
        head = create_node_list(nums)
        print_node_list(rotate(head, k))


test()
