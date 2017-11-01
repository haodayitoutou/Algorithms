"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.
"""


def is_balanced(root):
    return find_height(root) != -1


def find_height(node):
    if not node:
        return 0
    left = find_height(node.left)
    if left == -1:
        return -1

    right = find_height(node.right)
    if right == -1:
        return -1

    if abs(left - right) > 1:
        return -1
    return max(left, right) + 1
