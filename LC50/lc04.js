function find_median(nums1, nums2) {
    if (nums1.length > nums2.length) {
        var temp = nums1;
        nums1 = nums2;
        nums2 = temp;
    }

    var m = nums1.length,
        n = nums2.length,
        imin = 0,
        imax = m,
        half = parseInt(Math.floor((m + n + 1)/2)),
        i,
        j;

    if (n === 0) {
        return "Invalid input";
    }

    while (imin <= imax) {
        i = parseInt(Math.floor((imin + imax) / 2));
        j = parseInt(half - i);
        if (i > 0 && nums1[i-1] > nums2[j]) {
            imax = i - 1;
        } else if (i < m && nums2[j-1] > nums1[i]) {
            imin = i + 1;
        } else {
            break;
        }
    }

    var left_max;
    if (i === 0) {
        left_max = nums2[j-1];
    } else if (j === 0) {
        left_max = nums1[i-1];
    } else {
        left_max = Math.max(nums1[i-1], nums2[j-1]);
    }

    if ((m+n) % 2 === 1) {
        return left_max;
    }

    var right_min;
    if (i === m) {
        right_min = nums2[j];
    } else if (j === n) {
        right_min = nums1[i];
    } else {
        right_min = Math.min(nums1[i], nums2[j]);
    }
    return (left_max + right_min) / 2;
}

function test() {
    var n1_list = [
        [],
        [],
        [1, 2],
        [3, 4],
        [1, 4, 12, 51],
        [1, 4, 12, 32, 44],
        [1, 4, 12, 21, 32, 44],
        [1, 1, 1]
    ];
    var n2_list = [
        [],
        [1],
        [3, 4],
        [1, 2, 3],
        [2],
        [15, 24, 34, 47, 65, 66],
        [15, 24, 34, 47, 65, 66],
        [2, 2, 2]
    ];

    for (var i=0; i<n1_list.length; i++) {
        var nums1 = n1_list[i];
        var nums2 = n2_list[i];
        var median = find_median(nums1, nums2);
        console.log(nums1);
        console.log(nums2);
        console.log(median);
        console.log("--------");
    }
}

test()