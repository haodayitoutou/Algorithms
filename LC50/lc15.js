function three_sum(nums) {
    nums.sort();
    var output = [],
        first, second, third;
    for (var i = 0; i < nums.length - 2; i++) {
        if (i !== 0 && nums[i] === nums[i-1]) {
            continue;
        }
        first = nums[i];
        target = -first;
        var j = i + 1;
        var k = nums.length - 1;
        while (j < k) {
            second = nums[j];
            third = nums[k];
            if (second + third === target) {
                output.push([first, second, third]);
                j += 1;
                k -= 1;
                while (j < k && nums[j] == second) {
                    j += 1;
                }
                while (j < k && nums[k] == third) {
                    k -= 1;
                }
            } else if (second + third < target) {
                j += 1;
            } else {
                k -= 1;
            }
        }
    }
    return output;
}


function test() {
    var nums_list = [
        [0, 0, 0],
        [-1, 0, 1, 2, -1, -4]
    ];
    for (var nums of nums_list) {
        console.log(nums);
        console.log(three_sum(nums));
    }
}


test();
