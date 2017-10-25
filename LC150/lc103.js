function zigzag(root) {
    if (root === null) {
        return [];
    }
    var output = [],
        level = [root],
        reverse = false,
        temp,
        values;
    while (level.length > 0) {
        temp = [];
        values = [];
        for (var node of level) {
            if (reverse) {
                values.unshift(node.val);
            } else {
                values.push(node.val);
            }
            
            if (node.left !== null) {
                temp.push(node.left);
            }
            if (node.right !== null) {
                temp.push(node.right);
            }
        }
        reverse = !reverse;
        level = temp;
        output.push(values);
    }
    return output;
}