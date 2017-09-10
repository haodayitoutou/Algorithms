function swap(nums, i, j) {
    var temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

function sortColors(nums) {
    var i = 0, j = 0, k = nums.length - 1;
    var temp;
    while (j <= k) {
        if (nums[i] === 0) {
            swap(nums, i, j);
            i += 1;
            j += 1;
        } else if (nums[i] == 1) {
            j += 1;
        } else {
            swap(nums, j, k);
            k -= 1;
        }
    }
}