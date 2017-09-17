/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
For example, given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
*/


function trap(nums) {
    var total = 0,
        left = 0,
        right = nums.length - 1,
        maxL = 0,
        maxR = 0;

    while (left < right) {
        if (nums[left] <= nums[right]) {
            if (nums[left] >= maxL) {
                maxL = nums[left];
            } else {
                total += maxL - nums[left];
            }
            left += 1;
        } else {
            if (nums[right] >= maxR) {
                maxR = nums[right];
            } else {
                total += maxR - nums[right];
            }
            right -= 1;
        }
    }

    return total;
}


function test() {
    var nums_list = [
        [0, 0, 0],
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 2]
    ];
    for (var nums of nums_list) {
        console.log(nums + ' --> ' + trap(nums));
    }
}


test();
