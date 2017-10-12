function symmetric(left, right) {
    if (left === null && right === null) {
        return true;
    }
    if (left === null && right !== null) {
        return false;
    }
    if (left !== null && right === null) {
        return false;
    }
    if (left.val !== right.val) {
        return val;
    }
    return symmetric(left.left, right.right) && symmetric(left.right, right.left);
}

function isSymmetric(root) {
    if (root === null) {
        return true;
    }
    return symmetric(root.left, root.right);
}
