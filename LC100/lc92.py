"""
everse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""
from util import ListNode, create_node_list, print_node_list


def reverse(head, m, n):
    if m == n:
        return head

    dummy = ListNode(0)
    dummy.next = head

    pointer = dummy
    for _ in range(m - 1):
        pointer = pointer.next

    curr = pointer.next
    tail = None
    for _ in range(n - m + 1):
        temp = curr.next
        curr.next = tail
        tail = curr
        curr = temp

    pointer.next.next = curr
    pointer.next = tail
    return dummy.next


def test():
    head1 = create_node_list([1])
    print_node_list(reverse(head1, 1, 1))

    head2 = create_node_list([1, 2])
    print_node_list(reverse(head2, 1, 1))
    head2 = create_node_list([1, 2])
    print_node_list(reverse(head2, 1, 2))

    head3 = create_node_list([1, 2, 3])
    print_node_list(reverse(head3, 1, 2))
    head3 = create_node_list([1, 2, 3])
    print_node_list(reverse(head3, 1, 3))
    head3 = create_node_list([1, 2, 3])
    print_node_list(reverse(head3, 2, 3))

    head4 = create_node_list([1, 2, 3, 4, 5, 6, 7])
    print_node_list(reverse(head4, 1, 7))
    head4 = create_node_list([1, 2, 3, 4, 5, 6, 7])
    print_node_list(reverse(head4, 1, 4))
    head4 = create_node_list([1, 2, 3, 4, 5, 6, 7])
    print_node_list(reverse(head4, 3, 4))
    head4 = create_node_list([1, 2, 3, 4, 5, 6, 7])
    print_node_list(reverse(head4, 3, 7))


test()
