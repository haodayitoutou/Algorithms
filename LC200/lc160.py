"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
from util import ListNode, print_node_list


def intersect(head1, head2):
    pt1 = head1
    pt2 = head2

    while pt1 is not pt2:
        pt1 = head2 if pt1 is None else pt1.next
        pt2 = head1 if pt2 is None else pt2.next

    return pt1


def test():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)

    n1.next = n4
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    print_node_list(intersect(n1, n2))


test()
