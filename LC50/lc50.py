"""
Implement pow(x, n)
"""


def mypow(base, power):
    if power == 0:
        return 1
    if power < 0:
        power = -power
        base = 1 / base
    if power % 2 == 0:
        return mypow(base * base, power // 2)
    return mypow(base * base, power // 2) * base


print(pow(3, 2))
print(pow(3, -2))
print(pow(8.88023, 3))
