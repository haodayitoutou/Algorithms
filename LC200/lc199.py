r"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""
from util import create_tree_node


def view(node, level, output):
    if node:
        if level == len(output):
            output.append(node.val)
        view(node.right, level + 1, output)
        view(node.left, level + 1, output)


def right_view(root):
    output = []
    view(root, 0, output)
    return output


def test():
    nums_list = [
        [],
        [1, 2, 3],
        [1, 2, 3, 4, None, 5],
        [1, 2, 3, None, 4, 5, None, 6, 7, 8, 9, None, None, 10]
    ]
    for nums in nums_list:
        root = create_tree_node(nums)
        print(right_view(root))


test()
