"""
Sort a linked list using insertion sort.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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
        print_node_list(insert_sort(head))
        print("\n")


test()
