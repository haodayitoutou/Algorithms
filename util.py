"""
Utility functions
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, another):
        return self.val < another.val


def create_node_list(nums):
    if not nums:
        return None
    first = ListNode(nums[0])
    parent = first
    for i in range(1, len(nums)):
        new_node = ListNode(nums[i])
        parent.next = new_node
        parent = new_node

    return first


def print_node_list(head):
    output = []
    while head:
        output.append(head.val)
        head = head.next
    print(output)


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "TreeNode({})".format(self.val)


def create_tree_node(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    i = 1
    level = [root]
    while i < len(nums):
        for node in level:
            if node.left is None:
                node.left = TreeNode(nums[i])
                i += 1
                break
            elif node.right is None:
                node.right = TreeNode(nums[i])
                i += 1
                break
        else:
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = temp
    return root


def print_tree_node(root):
    output = []
    level = [root]
    while True:
        temp = []
        for lev in level:
            if lev:
                output.append(lev.val)
                temp.extend([lev.left, lev.right])
            else:
                output.append(None)
                temp.extend([None, None])
        level = temp
        if not any(level):
            break

    while output and output[-1] is None:
        output.pop()
    print(output)
