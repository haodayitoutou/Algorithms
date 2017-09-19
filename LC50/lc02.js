class ListNode {
    constructor(x) {
        this.val = x;
        this.next = null;
    }
}


function add_two(n1, n2) {
    var output = new ListNode(0);
    var first = output;
    var plus_one = false;
    var new_val, new_node;
    while (n1 !== null || n2 !== null) {
        new_val = 0;
        if (n1 !== null) {
            new_val += n1.val;
            n1 = n1.next;
        }
        if (n2 !== null) {
            new_val += n2.val;
            n2 = n2.next;
        }
        if (plus_one) {
            new_val += 1;
        }
        if (new_val >= 10) {
            new_val -= 10;
            plus_one = true;
        } else {
            plus_one = false;
        }
        new_node = new ListNode(new_val);
        first.next = new_node;
        first = new_node;
    }
    if (plus_one) {
        first.next = new ListNode(1);
    }
    return output.next;
}


function test() {
    // [2,4,3] +  [5,6,9]
    var n1_3 = new ListNode(3);
    var n1_2 = new ListNode(4);
    var n1_1 = new ListNode(2);
    n1_1.next = n1_2;
    n1_2.next = n1_3;

    var n2_3 = new ListNode(9);
    var n2_2 = new ListNode(6);
    var n2_1 = new ListNode(5);
    n2_1.next = n2_2;
    n2_2.next = n2_3;

    var total = add_two(n1_1, n2_1);
    while (total) {
        console.log(total.val);
        total = total.next;
    }
}


test();
