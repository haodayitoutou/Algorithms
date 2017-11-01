r"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
from util import create_tree_node


def has_path(root, total):
    if not root:
        return False
    if root.left is None and root.right is None and root.val == total:
        return True
    new_sum = total - root.val
    left = has_path(root.left, new_sum)
    right = has_path(root.right, new_sum)
    return left or right


def test():
    nums_list = [
        [],
        [],
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
    ]
    total_list = [
        0, 1, 21, 22, 26
    ]
    for nums, total in zip(nums_list, total_list):
        root = create_tree_node(nums)
        print(has_path(root, total))


test()
