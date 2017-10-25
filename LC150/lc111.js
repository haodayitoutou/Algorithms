function min_depth(root) {
    if (root === null) {
        return 0;
    }
    var left = min_depth(root.left);
    var right = min_depth(root.right);
    if (left === 0 || right === 0) {
        return left + right + 1;
    } else {
        return Math.min(left, right) + 1;
    }
}