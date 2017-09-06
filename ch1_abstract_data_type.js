
class Node {
    constructor(item=null) {
        this.item = item;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.first = null;
        this.N = 0;
    }

    isEmpty() {
        return (this.N === 0);
    }

    push(item) {
        var newNode = new Node(item);
        newNode.next = this.first;
        this.first = newNode;
        this.N += 1;
    }

    pop() {
        var item = this.first.item;
        this.first = this.first.next;
        this.N -= 1;
        return item;
    }

    get length() {
        return this.N;
    }

    *[Symbol.iterator]() {
        var cur = this.first;
        while (cur !== null) {
            var item = cur.item;
            cur = cur.next;
            yield item;
        }
    }
}

class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.N = 0;
    }

    enqueue(item) {
        var newNode = new Node(item);
        if (this.first !== null) {
            this.last.next = newNode;
        } else {
            this.first = newNode;
        }
        this.last = newNode;
        this.N += 1;
    }

    dequeue() {
        if (this.length === 0) {
            return null;
        }
        var item = this.first.item;
        this.first = this.first.next;
        if (this.length === 1) {
            this.last = null;
        }
        this.N -= 1;
        return item;
    }

    get length() {
        return this.N;
    }

    *[Symbol.iterator]() {
        var cur = this.first;
        while (cur !== null) {
            var item = cur.item;
            cur = cur.next;
            yield item;
        }
    }
}

class Bag {
    constructor() {
        this.first = null;
        this.N = 0;
    }

    add(item) {
        var newNode = new Node(item);
        newNode.next = this.first;
        this.first = newNode;
        this.N += 1;
    }

    get length() {
        return this.N;
    }

    *[Symbol.iterator]() {
        var cur = this.first;
        while (cur !== null) {
            var item = cur.item;
            cur = cur.next;
            yield item;
        }
    }
}


var testNode = function() {
    var n1 = new Node();
    console.log(n1);

    var n2 = new Node("a");
    console.log(n2);
    
    var n3 = new Node(23);
    console.log(n3);
    
    var n4 = new Node([2, 3]);
    console.log(n4);
    
    var n5 = new Node( {"a":1, "b":2});
    console.log(n5);
    
    class TestClass {
        constructor() {
            this.N = 0;
        }
    }

    var n6 = new Node( new TestClass() );
    console.log(n6);
};

var testStack = function() {
    var input = "ABCDEFG";

    var stack = new Stack();

    console.log("Push one item and pop it");
    stack.push(input[0]);
    console.log(stack.pop());

    console.log("Push all");
    for (var a of input) {
        stack.push(a);
        console.log(stack.first.item);
    }

    console.log("Test length method");
    console.log(stack.length);

    console.log("Test iterator");
    for (var item of stack) {
        console.log(item);
    }

    console.log("Pop all");
    while (stack.length > 0) {
        console.log(stack.pop());
    }
    console.log(stack);
};

var testQueue = function() {
    var input = "abcdefg";

    var queue = new Queue();

    console.log("Enqueue one item and dequeue it");
    queue.enqueue(input[0]);
    console.log(queue.dequeue());

    console.log("Enqueue all");
    for (var a of input) {
        queue.enqueue(a);
        console.log([queue.first, queue.last]);
    }

    console.log("Test length method");
    console.log(queue.length);

    console.log("Test iterator");
    for (var item of queue) {
        console.log(item);
    }

    console.log("Dequeue all");
    while (queue.length > 0) {
        console.log(queue.dequeue());
    }
};

var testBag = function() {
    var input = [1, 2, 3, 4, 5, 6, 7];
    var bag = new Bag();

    for (var n of input) {
        bag.add(n);
    }

    console.log("Test length method");
    console.log(bag.length);

    console.log("Test iterator");
    for (var item of bag) {
        console.log(item);
    }
};

var Test = function() {
    console.log("Test Node class");
    testNode();
    console.log("Test Stack class");
    testStack();
    console.log("Test Queue class");
    testQueue();
    console.log("Test Bag class");
    testBag();
};

Test();






