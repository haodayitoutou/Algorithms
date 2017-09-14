function maximum_gap(nums) {
    if (nums.length < 2) {
        return 0;
    }
    var N = nums.length;
    var minimum = Math.min(...nums);
    var maximum = Math.max(...nums);
    if (minimum === maximum) {
        return 0;
    }
    var gap = parseInt(Math.ceil(parseFloat(maximum-minimum)/(N-1)));
    var num_buckets = parseInt(Math.ceil(parseFloat(maximum-minimum) / gap));
    var bucket_min = new Array(num_buckets).fill(null);
    var bucket_max = new Array(num_buckets).fill(null);
    var index, curMin, curMax;
    for (var number of nums) {
        if (number === minimum || number === maximum) {
            continue;
        }
        index = Math.floor((number - minimum) / gap);
        curMin = bucket_min[index];
        curMax = bucket_max[index];
        if (curMin === null) {
            bucket_min[index] = number;
            bucket_max[index] = number;
        } else {
            bucket_min[index] = Math.min(curMin, number);
            bucket_max[index] = Math.max(curMax, number);
        }
    }
    var max_gap = 0;
    var previous = minimum;
    for (var i=0; i<num_buckets; i++) {
        if (bucket_min[i] === null) {
            continue;
        }
        max_gap = Math.max(max_gap, bucket_min[i] - previous);
        previous = bucket_max[i];
    }
    return Math.max(max_gap, maximum - previous);
}

function test() {
    var nums_list = [
        [],
        [1, 1],
        [10, 21, 17, 13, 22, 23, 28, 30],
        [1, 1, 1, 1, 5, 5, 5, 5],
        [41, 42, 81],
        [2, 6]
    ];

    for (var nums of nums_list) {
        console.log(maximum_gap(nums));
    }
}

test();