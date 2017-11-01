r"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree

Note:
You may only use constant extra space.

For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""


def connect(root):
    if not root:
        return
    head = root
    while head:
        curr = head
        head = None
        prev = None

        while curr:
            if curr.left:
                if prev:
                    prev.next = curr.left
                else:
                    head = curr.left
                prev = curr.left

            if curr.right:
                if prev:
                    prev.next = curr.right
                else:
                    head = curr.right
                prev = curr.right

            curr = curr.next
