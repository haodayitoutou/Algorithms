function largest(nums) {
    nums.push(0);
    var stack = [0];
    var res = 0;
    var height, width;
    for (var i=1; i<nums.length; i++) {
        while (stack.length > 0 && nums[i] < nums[stack.slice(-1)[0]]) {
            height = nums[stack.pop()];
            if (stack.length === 0) {
                width = i;
            } else {
                width = i - 1 - stack.slice(-1)[0];
            }
            if (width * height > res) {
                res = width * height;
            }
        }
        stack.push(i);
    }
    return res;
}


function test() {
    var nums_list = [
        [],
        [2, 1, 5, 6, 2, 3],
        [1, 1],
        [5, 1, 5],
        [1, 5, 1],
        [1, 2, 3, 4, 5],
        [4, 5, 6, 3, 6, 7, 8, 2]
    ];
    for (var nums of nums_list) {
        console.log(largest(nums));
    }
}


test();
