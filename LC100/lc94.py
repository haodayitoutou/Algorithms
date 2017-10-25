r"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2]
"""
from util import create_tree_node


def traversal_recursively(root):
    res = []
    dfs(root, res)
    return res


def dfs(node, res):
    if node:
        dfs(node.left, res)
        res.append(node.val)
        dfs(node.right, res)


def traversal_iteratively(root):
    stack = []
    res = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res


def test():
    nums_list = [
        [],
        [1, None, 2, 3],
        [28, 11, 32, 4, 25]
    ]
    for nums in nums_list:
        root = create_tree_node(nums)
        print(traversal_recursively(root))
        print(traversal_iteratively(root))


test()
