"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""


def get_permutation(num, kth):
    numbers = list(range(1, num + 1))
    factorial = [1] * (num + 1)

    product = 1
    for i in range(1, num + 1):
        product *= i
        factorial[i] = product

    permutation = []
    kth -= 1
    for i in range(1, num + 1):
        index = kth // factorial[num - i]
        permutation.append("{}".format(numbers.pop(index)))
        kth -= index * factorial[num - i]

    return "".join(permutation)
