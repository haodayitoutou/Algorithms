
function sink(nums, index, N) {
    var temp;
    while (index <= Math.floor(N/2)) {
        var j = index * 2;
        if (j < N && nums[j] < nums[j+1]) {
            j += 1;
        }
        if (nums[index] >= nums[j]) {
            break;
        }
        temp = nums[index];
        nums[index] = nums[j];
        nums[j] = temp;
        index = j;
    }
}

function heapsort(nums) {
    var N = nums.length - 1;
    for (var k = Math.floor(N/2); k>0; k--) {
        sink(nums, k, N);
    }
    var temp;
    while (N > 1) {
        temp = nums[1];
        nums[1] = nums[N];
        nums[N] = temp;
        N -= 1;
        sink(nums, 1, N);        
    }

    return nums;
}

console.log(
    heapsort(["0", "S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"])
);
