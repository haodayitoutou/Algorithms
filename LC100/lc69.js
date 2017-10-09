function sqrt(x) {
    if (x === 0) {
        return 0;
    }
    var low = 0, high = x, mid;
    while (low <= high) {
        mid = low + Math.floor((high - low)/2);
        if (mid * mid > x) {
            high = mid - 1;
        } else {
            if ((mid + 1) * (mid + 1) > x) {
                return mid;
            }
            low = mid + 1;
        }
    }
}


console.log(sqrt(0));
console.log(sqrt(1));
console.log(sqrt(3));
console.log(sqrt(10));
console.log(sqrt(48));
