class ListNode {
    constructor(x) {
        this.val = x;
        this.next = null;
    }
}


function reverse(head, m, n) {
    var dummy = new ListNode(0);
    dummy.next = head;

    var pointer = dummy;
    for (var i=0; i<m-1; i++) {
        pointer = pointer.next;
    }

    var curr = pointer.next;
    var tail = null;
    var temp;
    for (var j=0; j<n-m+1; j++) {
        temp = curr.next;
        curr.next = tail;
        tail = curr;
        curr = temp;
    }
    pointer.next.next = curr;
    pointer.next = tail;
    return dummy.next;
}
