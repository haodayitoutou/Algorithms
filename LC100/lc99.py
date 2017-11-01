"""
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.
"""
from util import create_tree_node, print_tree_node


def recover(root):
    stack = []
    first = None
    second = None
    prev = None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.val <= prev.val:
            if not first:
                first = prev
                second = root
            else:
                second = root
        prev = root
        root = root.right
    first.val, second.val = second.val, first.val


def test():
    nums_list = [
        [0, 1],
        [100, 50, 150, 25, 175, 125, 75]
    ]
    for nums in nums_list:
        root = create_tree_node(nums)
        print_tree_node(root)
        recover(root)
        print_tree_node(root)


test()
