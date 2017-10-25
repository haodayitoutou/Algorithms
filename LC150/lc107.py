r"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
from util import create_tree_node


def traversal(root):
    res = []
    dfs(res, root, -1)
    return res


def dfs(res, node, height):
    if not node:
        return
    if -1 * height > len(res):
        res.insert(0, [])
    res[height].append(node.val)
    dfs(res, node.left, height - 1)
    dfs(res, node.right, height - 1)


def test():
    nums_list = [
        [],
        [1],
        [1, 2, 2],
        [1, 2, 3, 4, None, 8],
        [3, 9, 20, None, None, 15, 7]
    ]
    for nums in nums_list:
        root = create_tree_node(nums)
        print(traversal(root))


test()
