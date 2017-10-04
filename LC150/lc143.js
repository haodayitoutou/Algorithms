function reorder(head) {
    if (head === null) {
        return head;
    }
    var pt1 = head, pt2 = head;
    while (pt2.next !== null && pt2.next.next !== null) {
        pt1 = pt1.next;
        pt2 = pt2.next.next;
    }

    var tail = null, curr = pt1.next, temp;
    while (curr !== null) {
        temp = curr.next;
        curr.next = tail;
        tail = curr;
        curr = temp;
    }
    pt1.next = tail;

    var pt0 = head;
    while (pt0 !== pt1) {
        temp = pt1.next;
        pt1.next = temp.next;
        temp.next = pt0.next;
        pt0.next = temp.next;

        pt0 = temp.next;
    }
    return head;
}