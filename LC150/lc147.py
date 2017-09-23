"""
Sort a linked list using insertion sort.
"""
from util import ListNode, create_node_list, print_node_list


def insert_sort(head):
    if head is None:
        return

    auxiliary = ListNode(0)
    auxiliary.next = head

    parent = auxiliary
    current = head
    while current and current.next:
        value = current.next.val
        if value >= current.val:
            current = current.next
            continue

        if value < parent.val:
            parent = auxiliary

        while value > parent.next.val:
            parent = parent.next

        # parent - parent.next -- cur - cur.next - cur.next.next
        # A      - B           -- C   - D        - E
        temp = current.next       # D
        current.next = temp.next  # A - B -- C - E, D
        temp.next = parent.next   # A - B -- C - E, D - B
        parent.next = temp        # A - D - B -- C - E

    return auxiliary.next


def test():
    numbers = [11, 21, 31, 31, 41, 51, 61, 71]

    import random
    for _ in range(10):
        random.shuffle(numbers)

        head = create_node_list(numbers)
        print("Before sort")
        print_node_list(head)
        print("After sort")
        print_node_list(insert_sort(head))
        print("\n")


test()
