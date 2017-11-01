r"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""


def flatten(root):
    if not root:
        return

    left = root.left
    right = root.right

    flatten(left)
    flatten(right)

    root.right = left
    root.left = None

    while root.right:
        root = root.right
    root.right = right
