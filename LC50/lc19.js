function remove(head, n) {
    var previous = head;
    var end = head;
    for (var i=0; i<n; i++) {
        end = end.next;
    }
    if (end === null) {
        return head.next;
    }
    while (end.next) {
        previous = previous.next;
        end = end.next;
    }
    previous.next = previous.next.next;
    return head;
}
