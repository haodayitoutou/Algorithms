"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
from util import ListNode, create_node_list, print_node_list


def partition(head, x):
    dummy1 = ListNode(0)
    dummy2 = ListNode(0)

    pt1, pt2 = dummy1, dummy2
    cur = head
    while cur:
        if cur.val < x:
            pt1.next = cur
            pt1 = cur
        else:
            pt2.next = cur
            pt2 = cur
        cur = cur.next
    pt2.next = None
    pt1.next = dummy2.next
    return dummy1.next


def test():
    nums_list = [
        [],
        [2, 4, 3, 4],
        [2, 4, 3, 4],
        [1, 4, 3, 2, 5, 2],
        [1, 4, 3, 2, 5, 2]
    ]
    x_list = [
        0, 3, 4, 4, 3
    ]
    for nums, x in zip(nums_list, x_list):
        head = create_node_list(nums)
        print_node_list(partition(head, x))


test()
