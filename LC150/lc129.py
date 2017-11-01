"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25
"""


def sum_numbers(root):
    return path(root, "")


def path(node, string):
    if not node:
        return 0
    string += int(node.val)
    if node.left is None and node.right is None:
        return int(string)
    return path(node.left, string) + path(node.right, string)
