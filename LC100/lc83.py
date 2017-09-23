"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
from util import create_node_list, print_node_list


def delete_duplicate(head):
    curr = head
    while curr:
        if curr.next and curr.next.val == curr.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


def test():
    nums_list = [
        [],
        [0],
        [0, 0],
        [0, 1, 2, 3, 3],
        [0, 0, 1, 1, 2, 2, 2, 3, 4, 5, 5, 5]
    ]

    for nums in nums_list:
        head = create_node_list(nums)
        new = delete_duplicate(head)
        print_node_list(new)


test()
