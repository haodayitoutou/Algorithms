"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


def sqrt(number):
    if number == 0:
        return 0
    low = 0
    high = number
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid > number:
            high = mid - 1
        else:
            if (mid + 1) * (mid + 1) > number:
                return mid
            low = mid + 1


print(sqrt(0))
print(sqrt(1))
print(sqrt(3))
print(sqrt(10))
print(sqrt(48))
