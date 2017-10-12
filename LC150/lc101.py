r"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""


from util import create_tree_node


def symmetric(left, right):
    if left is None and right is None:
        return True
    if (left and not right) or (not left and right):
        return False
    if left.val != right.val:
        return False
    return symmetric(left.left, right.right) and symmetric(left.right, right.left)


def is_symmetric(root):
    return root is None or symmetric(root.left, root.right)


def test():
    nums_list = [
        [],
        [1],
        [1, 2, 2],
        [1, 2, 3],
        [1, 2, 2, 3, 4, 4, 3],
        [1, 2, 2, 3, 3, 4, 4],
        [1, 2, 2, None, 3, None, 3],
        [1, 2, 2, None, 3, 3, None]
    ]
    for nums in nums_list:
        root = create_tree_node(nums)
        print(is_symmetric(root))


test()
