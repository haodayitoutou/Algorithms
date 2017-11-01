"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""
from util import create_node_list, TreeNode, print_tree_node


def linked_to_bst(head):
    if not head:
        return None

    length, temp = 0, head
    while temp:
        length += 1
        temp = temp.next
    root, _ = linked_to_bst_help(head, 0, length - 1)
    return root


def linked_to_bst_help(node, low, high):
    if low > high:
        return None, node

    mid = low + (high - low) // 2
    left, node = linked_to_bst_help(node, low, mid - 1)

    root = TreeNode(node.val)
    root.left = left

    node = node.next
    right, node = linked_to_bst_help(node, mid + 1, high)
    root.right = right
    return root, node


def test():
    nums_list = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6]
    ]
    for nums in nums_list:
        head = create_node_list(nums)
        root = linked_to_bst(head)
        print_tree_node(root)


test()
