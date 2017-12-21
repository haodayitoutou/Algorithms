"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     "1"
2.     "11"
3.     "21"
4.     "1211"
5.     "111221"
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""


def count_say(n):
    output = "1"
    for _ in range(1, n):
        output = generate(output)
    return output


def generate(number):
    # number is a string
    output = []
    i = 0
    while i < len(number):
        count = 1
        while i + 1 < len(number) and number[i + 1] == number[i]:
            i += 1
            count += 1
        output.extend([str(count), number[i]])
        i += 1
    return "".join(output)
