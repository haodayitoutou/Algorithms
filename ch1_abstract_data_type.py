class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

    def __repr__(self):
        if hasattr(self.item, "__repr__"):
            return "Node: %s" % self.item
        return "Node"


class Stack:
    def __init__(self):
        self.first = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.first
        self.first = new_node
        self.count += 1

    def pop(self):
        item = self.first.item
        self.first = self.first.next
        self.count -= 1
        return item

    def __len__(self):
        return self.count

    def __iter__(self):
        cur = self.first
        while cur:
            item = cur.item
            cur = cur.next
            yield item

    def __getitem__(self, idx):
        cur = self.first
        i = 0
        while i < idx:
            cur = cur.next
            i += 1

        return cur.item

    def __repr__(self):
        return "Stack: %i items" % len(self)


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        new_node = Node(item)

        if self.count:
            self.last.next = new_node
        else:  # Empty queue
            self.first = new_node

        self.last = new_node
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return None
        item = self.first.item
        self.first = self.first.next
        if self.count == 1:
            self.last = None
        self.count -= 1
        return item

    def __len__(self):
        return self.count

    def __iter__(self):
        cur = self.first
        while cur:
            item = cur.item
            cur = cur.next
            yield item

    def __getitem__(self, idx):
        cur = self.first
        i = 0
        while i < idx:
            cur = cur.next
            i += 1

        return cur.item

    def __repr__(self):
        return "Queue: %i items" % len(self)


class Bag:
    def __init__(self):
        self.first = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.first
        self.first = new_node
        self.count += 1

    def __len__(self):
        return self.count

    def __iter__(self):
        cur = self.first
        while cur:
            item = cur.item
            cur = cur.next
            yield item

    def __getitem__(self, idx):
        cur = self.first
        i = 0
        while i < idx:
            cur = cur.next
            i += 1

        return cur.item

    def __repr__(self):
        return "Bag: %i items" % len(self)


def test_node():
    node1 = Node()
    print(node1)

    node2 = Node("a")
    print(node2)

    node3 = Node(23)
    print(node3)

    node4 = Node([2, 3])
    print(node4)

    node5 = Node({"a": 1, "b": 2})
    print(node5)

    class TestClass:
        def __init__(self):
            self.count = 0

    node6 = Node(TestClass())
    print(node6)


def test_stack():
    a_string = "ABCDEFG"

    stack = Stack()

    print("Push one item and pop it")
    stack.push(a_string[0])
    print(stack.pop())

    print("Push all")
    for letter in a_string:
        stack.push(letter)
        print(stack.first)

    print("Test __len__")
    print(len(stack))

    print("Test __get__")
    print(stack[3])

    print("Test __iter__")
    print([item for item in stack])

    print("Pop all")
    while not stack.is_empty():
        print(stack.pop())


def test_queue():
    a_string = "abcdefg"

    queue = Queue()

    print("Enqueue one item and dequeue it")
    queue.enqueue(a_string[0])
    print(queue.dequeue())

    print("Enqueu all")
    for letter in a_string:
        queue.enqueue(letter)
        print([queue.first, queue.last])

    print("Test __len__")
    print(len(queue))

    print("Test __get__")
    print(queue[3])

    print("Test __iter__")
    print([item for item in queue])

    print("Dequeue all")
    while not queue.is_empty():
        print(queue.dequeue())


def test_bag():
    a_list = [1, 2, 3, 4, 5, 6, 7]
    bag = Bag()

    for num in a_list:
        bag.add(num)

    print(len(bag))
    print(bag[4])
    print([item for item in bag])


def test():
    print("Test Node")
    test_node()
    print("Test Stack")
    test_stack()
    print("Test Queue")
    test_queue()
    print("Test Bag")
    test_bag()


test()
