function searchRange(nums, target) {
    if (nums.length === 0) {
        return [-1, -1];
    }
    var low, high, mid, start;
    low = 0;
    high = nums.length - 1;
    while (low < high) {
        mid = low + Math.floor((high - low) / 2);
        if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    if (nums[low] !== target) {
        return [-1, -1];
    }
    start = low;

    high = nums.length - 1;
    while (low < high) {
        mid = low + Math.floor((high - low) / 2);
        if (nums[mid] > target) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    if (nums[low] !== target) {
        low -= 1;
    }
    return [start, low];
}


function test() {
    var nums_list = [
        [],
        [2, 3],
        [11, 12],
        [8],
        [8, 8],
        [8, 8, 8],
        [7, 8, 9],
        [4, 5, 7, 8, 8, 9, 10],
        [5, 6, 8, 8],
        [8, 8, 9, 10],
        [1, 3, 5, 6, 7, 8]
    ];
    for (var nums of nums_list) {
        console.log(searchRange(nums, 8));
    }
}


test();
