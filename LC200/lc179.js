function largest_number(nums) {
    if (nums.length === 0) {
        return "";
    }
    nums = nums.map((element) => {
        return element.toString();
    });
    nums.sort((string1, string2) => {
        var number1 = parseInt(string1.concat(string2));
        var number2 = parseInt(string2.concat(string1));
        return number2 - number1;
    });
    if (nums[0] === "0") {
        return "0";
    }
    return nums.join("");
}


function test() {
    var nums_list = [
            [],
            [1],
            [1, 0, 0],
            [0, 0],
            [3, 30, 34, 5, 9, 0],
            [21, 12, 23, 32]
        ];

    for (var nums of nums_list) {
        console.log(largest_number(nums));
    }
}


test();