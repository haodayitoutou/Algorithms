function maxArea(matrix) {
    var result = 0;
    if (matrix === null || matrix.length === 0 || matrix[0].length === 0) {
        return result;
    }

    var nCol = matrix[0].length;
    var nRow = matrix.length;
    var height = Array(nCol+1).fill(0);
    var stack, height1, width;
    for (var row=0; row<nRow; row++) {
        for (var col=0; col<nCol; col++) {
            if (matrix[row][col] === "1") {
                height[col] += 1;
            } else {
                height[col] = 0;
            }
        }

        stack = [0];
        for (var i=1; i<nCol+1; i++) {
            while (stack.length>0 && height[i] < height[stack.slice(-1)[0]]) {
                height1 = height[stack.pop()];
                if (stack.length === 0) {
                    width = i;
                } else {
                    width = i - 1 - stack.slice(-1)[0];
                }
                result = Math.max(result, height1 * width);
            }
            stack.push(i);
        }
    }
    return result;
}


function test() {
    var matrixs = [
        [],
        ["10100", "10111", "11111", "10010"],
        ["110101", "010011", "111101", "111101"]
    ];
    for (var matrix of matrixs) {
        console.log(maxArea(matrix));
    }
}


test();
