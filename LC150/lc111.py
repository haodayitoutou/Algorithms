"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
from util import create_tree_node


def min_depth(root):
    if root is None:
        return 0
    left = min_depth(root.left)
    right = min_depth(root.right)
    if left == 0 or right == 0:
        return left + right + 1
    else:
        return min(left, right) + 1


def test():
    nums_list = [
        [],
        [1],
        [1, 2, 2],
        [1, 2, 3, 4, None, 8],
        [3, 9, 20, None, None, 15, 7],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10]
    ]
    for nums in nums_list:
        root = create_tree_node(nums)
        print(min_depth(root))


test()
