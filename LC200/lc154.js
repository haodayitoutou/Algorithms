function search(nums) {
    var low = 0,
        high = nums.length - 1,
        mid;
    while (low < high) {
        mid = low + Math.floor((high - low) / 2);
        if (nums[mid] > nums[high]) {
            low = mid + 1;
        } else if (nums[mid] < nums[high]) {
            high = mid;
        } else {
            high -= 1;
        }
    }
    return nums[low];
}
