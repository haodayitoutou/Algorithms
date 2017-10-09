function search(matrix, target) {
    if (matrix.length === 0) {
        return false;
    }
    var Nrow = matrix.length,
        Ncol = matrix[0].length,
        low = 0,
        high = Nrow * Ncol - 1,
        mid, row, col, value;
    while (low <= high) {
        mid = low + Math.floor((high - low) / 2);
        row = Math.floor(mid / Ncol);
        col = mid % Ncol;
        value = matrix[row][col];
        if (value === target) {
            return true;
        } else if (value < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return false;
}


function test() {
    var matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ];
    var target_list = [
        0, 1, 2, 3, 4, 7, 10, 15, 16, 20, 23, 30, 36, 50, 51
    ];
    for (var target of target_list) {
        console.log(target, search(matrix, target));
    }
    // console.log(search(matrix, 3));
}


test();
