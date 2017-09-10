class ListNode {
    constructor(item) {
        this.val = item;
        this.next = null;
    }
}

function sort(head) {
    if (head === null || head.next === null) {
        return head;
    }

    var parent = null, mid = head, last = head;
    while (last !== null && last.next !== null) {
        parent = mid;
        mid = mid.next;
        last = last.next.next;
    }
    parent.next = null;

    head = sort(head);
    mid = sort(mid);
    return merge(head, mid);
}

function merge(head1, head2) {
    var first, parent;
    if (head1.val <= head2.val) {
        first = head1;
        head1 = head1.next;
    } else {
        first = head2;
        head2 = head2.next;
    }
    parent = first;

    while (head1 !== null && head2 !== null) {
        if (head1.val <= head2.val) {
            parent.next = head1;
            head1 = head1.next;
        } else {
            parent.next = head2;
            head2 = head2.next;
        }
        parent = parent.next;
    }

    if (head1 === null) {
        parent.next = head2;
    } else {
        parent.next = head1;
    }
    return first;
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

    head = sort(head);
    while (head !== null) {
        console.log(head.val);
        head = head.next;
    }
}

test();