class ListNode {
    constructor(x) {
        this.val = x;
        this.next = null;
    }
}


function partition(head, x) {
    var dummy1 = new ListNode(0),
        dummy2 = new ListNode(0);
    var pt1 = dummy1, pt2 = dummy2, curr = head;
    while (curr !== null) {
        if (curr.val < x) {
            pt1.next = curr;
            pt1 = pt1.next;
        } else {
            pt2.next = curr;
            pt2 = pt2.next;
        }
        curr = curr.next;
    }

    pt1.next = dummy2.next;
    pt2.next = null;
    return dummy1.next;
}
