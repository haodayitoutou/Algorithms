class Node:
    def __init__(self, key, val, N):
        self.key = key
        self.val = val
        self.count = N
        self.left = None
        self.right = None


class BST:
    @property
    def size(self):
        if self.root:
            return self.root.count
        return 0

    def __init__(self):
        self.root = None

    def get(self, key):

        def _get(node, key):
            if node is None:
                return None
            if key < node.key:
                return _get(node.left, key)
            elif key > node.key:
                return _get(node.right, key)
            return node.val

        return _get(self.root, key)

    def put(self, key, val):

        def _put(node, key, val):
            if node is None:
                return Node(key, val, 1)
            if key < node.key:
                node.left = _put(node.left, key, val)
            elif key > node.key:
                node.right = _put(node.right, key, val)
            else:
                node.val = val
            node.count = node.left.count + node.right.count + 1
            return node

        self.root = _put(self.root, key, val)
