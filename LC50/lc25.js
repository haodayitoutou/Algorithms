class ListNode {
    constructor(item) {
        this.val = item;
        this.next = null;
    }
}


function swap(head, k) {
    var dummy = ListNode(0);
    dummy.next = head;
    var jump = dummy;
    var curr_first = head;
    var next_first = head;

    var count, parent, child, i, temp;
    while (true) {
        count = 0;
        while (next_first !== null && count < k) {
            count += 1;
            next_first = next_first.next;
        }
        if (count === k) {
            parent = curr_first;
            child = next_first;
            for (i=0; i<k; i++ ) {
                temp = parent.next;
                parent.next = child;
                child = parent;
                parent = temp;
            }
            jump.next = child;
            jump = curr_first;
            curr_first = next_first;
        } else {
            return dummy.next;
        }
    }
}
