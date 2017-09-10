"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def sort(head):
    if head is None or head.next is None:
        return head

    parent, mid, last = None, head, head
    while last and last.next:
        parent = mid
        mid = mid.next
        last = last.next.next

    parent.next = None
    head = sort(head)
    mid = sort(mid)
    return merge(head, mid)


def merge(head1, head2):
    if head1.val <= head2.val:
        first = head1
        head1 = head1.next
    else:
        first = head2
        head2 = head2.next

    parent = first
    while head1 and head2:
        if head1.val <= head2.val:
            parent.next = head1
            head1 = head1.next
        else:
            parent.next = head2
            head2 = head2.next
        parent = parent.next

    if head1 is None:
        parent.next = head2
    else:
        parent.next = head1
    return first


def create_node_list(nums):
    first = ListNode(nums[0])
    parent = first
    for i in range(1, len(nums)):
        new_node = ListNode(nums[i])
        parent.next = new_node
        parent = new_node

    return first


def print_node_list(head):
    output = []
    while head:
        output.append(head.val)
        head = head.next
    print(output)


def test():
    numbers = [11, 21, 31, 31, 41, 51, 61, 71]

    import random
    for _ in range(10):
        random.shuffle(numbers)

        head = create_node_list(numbers)
        print("Before sort")
        print_node_list(head)
        print("After sort")
        print_node_list(sort(head))
        print("\n")


test()
