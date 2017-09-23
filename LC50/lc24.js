class ListNode {
    constructor(item) {
        this.val = item;
        this.next = null;
    }
}


function swap(node) {
    if (node === null || ndoe.next === null) {
        return node;
    }

    var dummy = ListNode(0);
    var previous = dummy;
    var first = node;
    var second = node.next;
    var third;
    while (first !== null && second !== null) {
        third = second.next;

        previous.next = second;
        second.next = first;
        first.next = third;

        if (third !== null) {
            previous = first;
            first = third;
            second = third.next;
        } else {
            break;
        }
    }
    return dummy.next;
}
