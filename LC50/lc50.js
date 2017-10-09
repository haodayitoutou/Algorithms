function pow(x, n) {
    if (n === 0) {
        return 1;
    }
    if (n < 0) {
        n = -n;
        x = 1 / x;
    }
    if (n % 2 === 0) {
        return pow(x*x, Math.floor(n/2));
    } else {
        return x * pow(x*x, Math.floor(n/2));
    }
}

console.log(pow(3, 2))
console.log(pow(3, -2))
console.log(pow(8.88023, 3))
