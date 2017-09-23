"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
from util import ListNode, create_node_list, print_node_list


def swap(node):
    if node is None or node.next is None:
        return node
    dummy = ListNode(0)
    first = dummy

    previous = dummy
    first = node
    second = node.next
    while first and second:
        third = second.next

        # pre - 1st - 2nd - 3rd  -->
        # pre - 2nd - 1st - 3rd
        previous.next = second  # pre - 2nd - 3rd, 1st - 2nd - 3rd
        second.next = first  # pre - 2nd <-> 1st, 3rd
        first.next = third  # pre - 2nd - 1st - 3rd

        if third:
            previous = first
            first = third
            second = third.next
        else:
            break

    return dummy.next


def test():
    nums_list = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5]
    ]

    for nums in nums_list:
        node = create_node_list(nums)
        print_node_list(swap(node))


test()
