function traversal(root) {
    if (root === null) {
        return [];
    }
    var res = [],
        queue = [root],
        values,
        node,
        levelNum;
    while (queue.length > 0) {
        values = [];
        levelNum = queue.length;
        for (var i = 0; i < levelNum; i++) {
            node = queue.shift();
            values.push(node.val);
            if (node.left !== null) {
                queue.push(node.left);
            }
            if (node.right !== null) {
                queue.push(node.right);
            }
        }
        res.unshift(values);
    }
    return res;
}
