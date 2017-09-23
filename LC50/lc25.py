"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
from util import ListNode, create_node_list, print_node_list


def swap(node, k):
    dummy = ListNode(0)
    dummy.next = curr_first = next_first = node
    jump = dummy

    while True:
        count = 0
        while next_first and count < k:
            count += 1
            next_first = next_first.next

        if count == k:
            parent = curr_first
            child = next_first

            for _ in range(k):
                temp = parent.next
                parent.next = child
                child = parent
                parent = temp

            jump.next = child
            jump = curr_first
            curr_first = next_first
        else:
            return dummy.next


def test():
    nums_list = [
        [],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [1, 2, 3, 4, 5, 6]
    ]
    k_list = [
        1, 4, 4, 6
    ]
    for nums, k in zip(nums_list, k_list):
        node = create_node_list(nums)
        print_node_list(swap(node, k))


test()
