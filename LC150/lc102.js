function traversal(root) {
    if (root === null) {
        return [];
    }
    var res = [],
        level = [root],
        values,
        node,
        temp;
    while (level.length > 1) {
        values = [];
        for (node of level) {
            values.push(node.val);
        }
        res.push(values);

        temp = [];
        for (node of level) {
            if (node.left !== null) {
                temp.push(node.left);
            }
            if (node.right !== null) {
                temp.push(node.right);
            }
        }
        level = temp;
    }
    return res;
}