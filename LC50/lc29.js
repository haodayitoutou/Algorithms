function divide(dividend, divisor) {
    if (divisor === 0 || (dividend === -(2**31) && divisor === -1)) {
        return 2**31-1;
    }
    var positive = (dividend > 0 === divisor > 0);
    dividend = Math.abs(dividend);
    divisor = Math.abs(divisor);

    var result = 0, temp, i;
    while (dividend >= divisor) {
        temp = divisor;
        i = 1;
        while (dividend >= temp + temp) {
            temp <<= 1;
            i <<= 1;
        }
        dividend -= temp;
        result += i;
    }
    if (positive === false) {
        result = -result;
    }
    return result;
}

console.log(divide(-(2**31), -1));
console.log(divide(12, 3));
