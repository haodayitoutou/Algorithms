"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
from util import TreeNode, print_tree_node


def array_to_bst(nums):
    if not nums:
        return None
    return bst_help(nums, 0, len(nums) - 1)


def bst_help(nums, low, high):
    if low > high:
        return None
    mid = low + (high - low) // 2
    root = TreeNode(nums[mid])
    root.left = bst_help(nums, low, mid - 1)
    root.right = bst_help(nums, mid + 1, high)
    return root


def test():
    nums_list = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5]
    ]
    for nums in nums_list:
        root = array_to_bst(nums)
        print_tree_node(root)


test()
