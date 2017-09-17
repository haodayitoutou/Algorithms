function isValid(s) {
    var stack = [];
    var pairs = {
        "]": "[",
        ")": "(",
        "}": "{"
    };
    var other_half;
    for (var char of s) {
        if (char in pairs) {
            other_half = pairs[char];
            if (stack.length === 0 || stack.slice(-1)[0] !== other_half) {
                return false;
            }
            stack.pop();
        } else {
            stack.push(char);
        }
    }
    return stack.length === 0;
}


function test() {
    var strings = [
        "[",
        "]",
        "[]",
        "][",
        "([{{}}])",
        "([{]})"
    ];
    for (var a_string of strings) {
        console.log(isValid(a_string));
    }
}


test();
