class ListNode {
    constructor(item) {
        this.val = item;
        this.next = null;
    }
}


function merge(num1, num2) {
    var output = new ListNode(0);
    var first = output;
    while (num1 !== null && num2 !== null) {
        if (num1.val < num2.val) {
            first.next = num1;
            num1 = num1.next;
        } else {
            first.next = num2;
            num2 = num2.next;
        }
        first = first.next;
    }
    if (num1 === null) {
        first.next = num2;
    } else {
        first.next = num1;
    }
    return output.next;
}

