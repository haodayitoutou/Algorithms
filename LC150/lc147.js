class ListNode {
    constructor(item) {
        this.val = item;
        this.next = null;
    }
}

function sort_linked_list(head) {
    var auxiliary = new ListNode(0);
    auxiliary.next = head;

    var parent = auxiliary;
    var current = head;
    var temp;
    while (current !== null && current.next !== null) {
        var value = current.next.val;
        if (value > current.val) {
            current = current.next;
            continue;
        }
        if (value < parent.next.val) {
            parent = auxiliary;
        }
        while (value > parent.next.val) {
            parent = parent.next;
        }
        temp = current.next;
        current.next = temp.next;
        temp.next = parent.next;
        parent.next = temp;
    }

    return auxiliary.next;
}

function test() {
    var numbers = [41, 61, 11, 21, 31, 31, 51, 71];
    var head = new ListNode(numbers[0]);
    var parent = head;
    for (var index = 1; index < numbers.length; index++) {
        var element = numbers[index];
        var newNode = new ListNode(element);
        parent.next = newNode;
        parent = newNode;
    }

    head = sort_linked_list(head);
    while (head !== null) {
        console.log(head.val);
        head = head.next;
    }
}

test();