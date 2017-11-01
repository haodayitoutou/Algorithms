"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


def max_depth(root):
    if not root:
        return 0

    depth = 0
    level = [root]
    while level:
        depth += 1
        temp = []
        for node in level:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        level = temp
    return depth
