"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""
from util import ListNode, create_node_list, print_node_list


def merge(list1, list2):
    output = ListNode(0)
    first = output
    while (list1 is not None) and (list2 is not None):
        if list1.val < list2.val:
            first.next = list1
            list1 = list1.next
        else:
            first.next = list2
            list2 = list2.next
        first = first.next

    if list1 is None:
        first.next = list2
    else:
        first.next = list1

    return output.next


def test():
    n1_list = [
        [],
        [1, 2, 3],
        [2, 9, 10, 11, 15],
        [3, 5, 7]
    ]
    n2_list = [
        [],
        [],
        [3, 5, 12],
        [2, 6, 8]
    ]

    for list1, list2 in zip(n1_list, n2_list):
        head1 = create_node_list(list1)
        head2 = create_node_list(list2)
        print_node_list(head1)
        print_node_list(head2)

        head3 = merge(head1, head2)
        print_node_list(head3)
        print("\n")


test()
