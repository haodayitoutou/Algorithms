r"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
from util import create_tree_node


def zigzag(root):
    if not root:
        return []
    level = [root]
    output = []
    reverse = False
    while level:
        values = [node.val for node in level]
        if reverse:
            values = values[::-1]
        output.append(values)
        reverse = not reverse

        temp = []
        for node in level:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        level = temp
    return output


def test():
    nums_list = [
        [],
        [1],
        [3, 9, 20, None, None, 15, 7],
        [1, 2, 3, 4, 5, 6, 7, 8, None, 9],
        [1, 2, None, None, 3, None, 4, 5, 6, 11, 12, 13]
    ]
    for nums in nums_list:
        root = create_tree_node(nums)
        print(zigzag(root))


test()
