"""
Utility functions
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, another):
        return self.val < another.val


def create_node_list(nums):
    if not nums:
        return None
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
