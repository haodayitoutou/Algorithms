function search(nums) {
    var low = 0,
        high = nums.length - 1,
        mid;
    while (low < high) {
        mid = low + Math.floor((high - low) / 2);
        if (nums[mid] < nums[high]) {
            high = mid;
        } else if (nums[mid] > nums[high]) {
            low = mid + 1;
        }
    }
    return nums[low];
}


function test() {
    var nums_list = [
        [1],
        [1, 2],
        [1, 2, 3],
        [3, 1],
        [3, 2, 1],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 1],
        [3, 4, 5, 1, 2],
        [4, 5, 1, 2, 3],
        [5, 1, 2, 3, 4]
    ];
    for (var nums of nums_list) {
        console.log(search(nums));
    }
}


test();
