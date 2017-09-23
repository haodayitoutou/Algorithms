"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
from util import ListNode, create_node_list, print_node_list


def merge(nodes):
    from queue import PriorityQueue

    dummy = ListNode(0)
    first = dummy

    queue = PriorityQueue()
    for node in nodes:
        if node:
            queue.put((node.val, node))

    while queue.qsize() > 0:
        first.next = queue.get()[1]
        first = first.next

        if first.next:
            queue.put((first.next.val, first.next))

    return dummy.next


def test():
    numbers = [
        [-10, -6, -4, -3, -3, -2, 4],
        [-9],
        [],
        [],
        [-9],
        [-6, -4, -2, -2, 0, 2, 5, 8],
        [-8, -3, 5, 9]
    ]
    nodes = [create_node_list(nums) for nums in numbers]
    print_node_list(merge(nodes))


test()
