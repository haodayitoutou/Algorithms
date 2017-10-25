r"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
    2
   / \
  1   3
return true.

Example 2:
    1
   / \
  2   3
return false.
"""
from util import create_tree_node


def is_valid(root):
    return validate(root, float('-inf'), float('inf'))


def validate(node, minimum, maximum):
    if not node:
        return True
    if node.val >= maximum or node.val <= minimum:
        return False
    return validate(node.left, minimum, node.val)\
        and validate(node.right, node.val, maximum)


def test():
    nums_list = [
        [],
        [1, 2, 3],
        [2, 1, 3],
        [1, None, 2, 3],
        [28, 11, 32, 4, 25],
        [22, 11, 32, 4, 25]
    ]
    for nums in nums_list:
        root = create_tree_node(nums)
        print(is_valid(root))


test()
