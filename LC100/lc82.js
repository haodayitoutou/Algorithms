class ListNode {
    constructor(x) {
        this.val = x;
        this.next = null;
    }
}

function remove_duplicate(head) {
    var dummy = ListNode(0);
    dummy.next = head;

    var previous = dummy;
    var curr = head;
    while (curr !== null) {
        while (curr.next !== null && curr.next.val === curr.val) {
            curr = curr.next;
        }
        if (previous.next === curr) {
            previous = curr;
        } else {
            previous.next = curr.next;
        }
        curr = curr.next;
    }
    return dummy.next;
}