function two_sum(nums, target) {
    var note = {};
    for (var i=0; i<nums.length; i++) {
        var number = nums[i];
        if (note.hasOwnProperty(number)) {
            var j = note[number];
            if (i < j) {
                return [i, j];
            }
            return [j, i];
        } else {
            note[target - number] = i;
        }
    } 
}


function test() {
    var nums_list = [
        [3, 2, 4],
        [2, 11, 53, 7],
        [1, 3, 4, 5, 42, 16, 17, 12]
    ];
    var target_list = [
        6, 9, 16
    ];
    for (var i=0; i<3; i++) {
        var nums = nums_list[i];
        var target = target_list[i];
        console.log(two_sum(nums, target));
    }
}


test();