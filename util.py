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
    queue = [root, root]
    i = 1
    assign_left = True
    while i < len(nums) and queue:
        value = nums[i]
        parent = queue.pop(0)
        if value is not None:
            new_node = TreeNode(value)
            if assign_left:
                parent.left = new_node
            else:
                parent.right = new_node
            queue.extend([new_node, new_node])
        assign_left = not assign_left
        i += 1

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
        level = temp
        if not any(level):
            break

    while output and output[-1] is None:
        output.pop()
    print(output)


def test():
    nums_list = [
        [1],
        [1, None, 3, None, 4],
        [1, None, None, 3],
        [1, 2, 3, 4, 5, 6, 7],
        [3, 9, 20, None, None, 15, 7],
        [1, 2, 2, None, 3, None, 3]
    ]
    for nums in nums_list:
        root = create_tree_node(nums)
        print_tree_node(root)


# test()
