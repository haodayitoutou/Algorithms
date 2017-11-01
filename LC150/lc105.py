"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
from util import TreeNode


def build(preorder, inorder):
    if not preorder:
        return None

    value = preorder.pop()
    idx = inorder.index(value)

    root = TreeNode(value)
    root.left = build(preorder, inorder[0:idx])
    root.right = build(preorder, inorder[idx + 1:])
    return root
