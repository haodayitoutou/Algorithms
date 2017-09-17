function max_container(nums) {
    var i = 0,
        j = nums.length - 1,
        max_volumn = 0,
        height;
    while (i < j) {
        height = Math.min(nums[i], nums[j]);
        max_volumn = Math.max(max_volumn, height * (j-i));
        if (nums[i] < nums[j]) {
            while (i < j && nums[i] <= height) {
                i += 1;
            }
        } else {
            while (i < j && nums[j] <= height) {
                j -= 1;
            }
        }
    }
    return max_volumn;
}

function test() {
    var nums_list = [
        [1, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 11, 2, 12, 3, 3, 16],
        [1, 11, 2, 12, 3, 6]
    ];

    for (var nums of nums_list) {
        console.log(max_container(nums));
    }
}

test();