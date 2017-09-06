function quickSort(nums, low, high) {
    if (low >= high) {
        return;
    }

    var i = low+1;
    var j = high;
    var value = nums[low];
    var temp;
    while (true) {
        while (nums[i] < value && i < high) {
            i += 1;
        }
        while (nums[j] > value) {
            j -= 1;
        }
        if (i >= j) {
            break;
        }
        temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    nums[low] = nums[j];
    nums[j] = value;
    
    quickSort(nums, low, j-1);
    quickSort(nums, j+1, high);
}

function quickSort3Way(nums, low, high) {
    if (low >= high) {
        return;
    }

    var lt = low;
    var gt = high;
    var i = low + 1;
    var value = nums[low];
    var temp;
    while (i <= gt) {
        if (nums[i] < value) {
            temp = nums[i];
            nums[i] = nums[lt];
            nums[lt] = temp;
            lt += 1;
            i += 1;
        } else if (nums[i] > value) {
            temp = nums[i];
            nums[i] = nums[gt];
            nums[gt] = temp;
            gt -= 1;
        } else {
            i += 1;
        }
    }
    quickSort3Way(nums, low, lt-1);
    quickSort3Way(nums, gt+1, high);
}

function test() {
    var nums = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O",
                 "P", "A", "S", "D", "F", "G", "H", "J", "K",
                 "L", "Z", "X", "C", "V", "B", "N", "M"];
    var high = nums.length - 1;
    quickSort(nums, 0, high);
    console.log(nums);

    nums = ["R", "B", "W", "W", "R", "W", "B", "R", "R", "W", "B", "R"];
    high = nums.length - 1;
    quickSort3Way(nums, 0, high);
    console.log(nums);
}

test();