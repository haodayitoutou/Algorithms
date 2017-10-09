function search_insert(nums, target) {
    var low = 0,
        high = nums.length - 1;
    var mid;
    while (low <= high) {
        mid = low + Math.floor((high-low)/2);
        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return low;
}


console.log(search_insert([], 1));
console.log(search_insert([1], 1));
console.log(search_insert([1, 3, 5, 6], 0));
console.log(search_insert([1, 3, 5, 6], 1));
console.log(search_insert([1, 3, 5, 6], 2));
console.log(search_insert([1, 3, 5, 6], 4));
console.log(search_insert([1, 3, 5, 6], 6));
console.log(search_insert([1, 3, 5, 6], 7));
