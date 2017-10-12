r"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from util import create_tree_node


def traversal(root):
    if not root:
        return []
    res = []
    level = [root]
    while level:
        res.append([node.val for node in level])

        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [node for node in temp if node]

    return res


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
