"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""


def is_same(root1, root2):
    return compare(root1, root2)


def compare(node1, node2):
    if node1 is None and node2 is None:
        return True
    if not node1 or not node2 or node1.val != node2.val:
        return False
    left = compare(node1.left, node2.left)
    right = compare(node1.right, node2.right)
    return left and right
