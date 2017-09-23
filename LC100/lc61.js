function rotate(head, k) {
    if (head === null || head.next === null || k === 0) {
        return head;
    }
    var pt1 = head;
    var length = 1;
    while (pt1.next !== null) {
        pt1 = pt1.next;
        length += 1;
    }

    k = k % length;
    if (k === 0) {
        return head;
    }

    var pt2 = head;
    for (var i=0; i<length-k-1; i++) {
        pt2 = pt2.next;
    }

    var new_head = pt2.next;
    pt2.next = null;
    pt1.next = head;
    return new_head;
}
