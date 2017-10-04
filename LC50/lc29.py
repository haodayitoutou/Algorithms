"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


def divide(dividend, divisor):
    if divisor == 0 or (dividend == -2 ** 31 and divisor == -1):
        return 2 ** 31 - 1
    positive = (dividend > 0) == (divisor > 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    result = 0
    while dividend > divisor:
        temp = dividend
        i = 1
        while dividend >= temp + temp:
            temp <<= 1
            i <<= 1
        dividend -= temp
        result += i

    if not positive:
        result = -result

    return result
