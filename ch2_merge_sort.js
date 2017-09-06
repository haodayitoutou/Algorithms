function merge(nums, low, mid, high) {
    var i = low;
    var j = mid + 1;
    var aux = [];

    for (var index = 0; index < high - low + 1; index++) {
        if (i > mid) {
            aux.push(nums[j]);
            j += 1;
        } else if (j > high) {
            aux.push(nums[i]);
            i += 1;
        } else if (nums[i] < nums[j]) {
            aux.push(nums[i]);
            i += 1;
        } else {
            aux.push(nums[j]);
            j += 1;
        }
    }

    //nums.splice(low, aux.length, *aux);
    //1 low: start point to delete
    //2 aux.length: number of elements to delete
    //3 unpack aux: insert elements of aux
    Array.prototype.splice.apply(nums, [low, aux.length].concat(aux));
}

function mergesort(nums, low, high) {
    if (low >= high) {
        return;
    }
    var mid = Math.floor((low + high) / 2);
    mergesort(nums, low, mid);
    mergesort(nums, mid+1, high);
    merge(nums, low, mid, high);
}

function test_merge() {
    var a_list = ["M", "E", "R", "G", "E", "S", "O", "R",
                  "T", "E", "X", "A", "M", "P", "L", "E"];

    mergesort(a_list, 0, a_list.length - 1);
    console.log(a_list);
}

test_merge();
