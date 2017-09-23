"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
from util import ListNode, create_node_list, print_node_list


def remove_duplicate(head):
    dummy = ListNode(0)
    dummy.next = head

    previous = dummy
    curr = head
    while curr:
        while curr.next and curr.next.val == curr.val:
            curr = curr.next

        if previous.next == curr:
            previous = curr
        else:
            previous.next = curr.next
        curr = curr.next

    return dummy.next


def test():
    nums_list = [
        [],
        [0],
        [1, 1, 1],
        [1, 2, 3, 4],
        [1, 1, 2, 2, 3, 3, 4, 4]
    ]
    for nums in nums_list:
        head = create_node_list(nums)
        print_node_list(remove_duplicate(head))


test()
