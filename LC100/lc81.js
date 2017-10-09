function search(nums, target) {
    if (nums.length === 0) {
        return false;
    }
    var low = 0,
        high = nums.length - 1,
        mid;
    while (low < high) {
        mid = low + Math.floor((high - low) / 2);
        if (nums[mid] === target) {
            return true;
        }
        if (nums[mid] > nums[low]) {
            if (target >= nums[low] && target < nums[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        } else if (nums[mid] < nums[low]) {
            if (target < nums[low] && target > nums[mid]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        } else {
            low += 1;
        }
    }
    return nums[low] === target ? true : false;
}


function test() {
    var nums1 = [9, 11, 13, 15, 21, 24, 3, 5, 7],
        nums2 = [8, 8, 8, 8, 13, 5, 7, 8],
        nums3 = [8, 19, 24, 6, 8, 8, 8, 8],
        target1, target2, target3;

    console.log(nums1);
    for (target1 of [1, 3, 4, 5, 7, 8, 12, 14, 20, 22, 24, 26]) {
        console.log(target1, search(nums1, target1));
    }
    console.log(nums2);
    for (target2 of [3, 5, 6, 7, 8, 9, 11, 13, 14, 15]) {
        console.log(target2, search(nums2, target2));
    }
    console.log(nums3);
    for (target3 of [3, 5, 7, 8, 9, 12, 19, 20, 22, 23, 24, 26]) {
        console.log(target3, search(nums3, target3));
    }
}


test();
