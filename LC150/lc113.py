r"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


def find_path(root, total):
    result = []
    find_path_help(root, total, [], result)
    return result


def find_path_help(node, total, curr, res):
    if not node:
        return

    curr.append(node.val)
    if node.val == total and node.left is None and node.right is None:
        res.append(curr[:])
        curr.pop()
        return

    find_path_help(node.left, total - node.val, curr, res)
    find_path_help(node.right, total - node.val, curr, res)
    curr.pop()
