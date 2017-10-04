function cycle(head) {
    if (head === null || head.next === null) {
        return null;
    }
    var pt1 = head, pt2 = head;
    while (true) {
        if (pt2.next === null || pt2.next.next === null) {
            return null;
        }
        pt1 = pt1.next;
        pt2 = pt2.next.next;
        if (pt1 === pt2) {
            break;
        }
    }
    var pt3 = head;
    while (pt2 !== pt3) {
        pt2 = pt2.next;
        pt3 = pt3.next;
    }
    return pt2;
}