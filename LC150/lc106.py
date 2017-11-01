"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
from util import TreeNode


def build(inorder, postorder):
    if not inorder:
        return None
    value = postorder.pop()
    idx = inorder.index(value)

    root = TreeNode(value)
    root.right = build(inorder[0:idx], postorder)
    root.left = build(inorder[idx + 1:], postorder)
    return root
