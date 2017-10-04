function cycle(head) {
    if (head === null) {
        return false;
    }
    var pt1 = head, pt2 = head;
    while (pt2.next !== null && pt2.next.next !== null) {
        pt1 = pt1.next;
        pt2 = pt2.next.next;
        if (pt1 === pt2) {
            return true;
        }
    }
    return false;
}