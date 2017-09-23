class ListNode {
    constructor(x) {
        this.val = x;
        this.next = null;
    }
}


function intersect(head1, head2) {
    var pt1 = head1,
        pt2 = head2;
    while (pt1 !== pt2) {
        if (pt1 === null) {
            pt1 = head2;
        } else {
            pt1 = pt1.next;
        }
        if (pt2 === null) {
            pt2 = head1;
        } else {
            pt2 = pt2.next;
        }
    }
    return pt1;
}


function test() {
    var n1 = new ListNode(1),
        n2 = new ListNode(2),
        n3 = new ListNode(3),
        n4 = new ListNode(4),
        n5 = new ListNode(5),
        n6 = new ListNode(6);
    n1.next = n4;
    n2.next = n3;
    n3.next = n4;
    n4.next = n5;
    n5.next = n6;

    var intersection = intersect(n1, n4);
    while (intersection !== null) {
        console.log(intersection.val);
        intersection = intersection.next;
    }
}


test();
