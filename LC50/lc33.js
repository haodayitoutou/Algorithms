function find(nums, target) {
    if (nums.length === 0) {
        return -1;
    }
    var low = 0, high = nums.length - 1, mid;
    while (low < high) {
        mid = low + Math.floor((high - low) / 2);
        if (nums[mid] >= nums[low]) {
            if (target >= nums[low] && target < nums[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        } else {
            if (target <= nums[high] && target > nums[mid]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }
    if (nums[low] === target) {
        return low;
    }
    return -1;
}


var nums = [11, 13, 15, 17, 2, 4, 6];
console.log(find(nums, 2));
console.log(find(nums, 3));
console.log(find(nums, 6));
console.log(find(nums, 7));
console.log(find(nums, 11));
console.log(find(nums, 14));
console.log(find(nums, 17));
console.log(find(nums, 18));
