function delete_duplicate(head) {
    var curr = head;
    while (curr !== null) {
        if (curr !== null && curr.val === curr.next.val) {
            curr.next = curr.next.next;
        } else {
            curr = curr.next;
        }
    }
    return head;
}