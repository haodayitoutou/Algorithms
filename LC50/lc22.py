"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def generate(number):
    result = []
    generate_help(result, "", 0, 0, number)
    return result


def generate_help(result, string, begin, end, maximum):
    if len(string) == 2 * maximum:
        result.append(string)
        return
    if begin < maximum:
        generate_help(result, string + "(", begin + 1, end, maximum)
    if end < begin:
        generate_help(result, string + ")", begin, end + 1, maximum)


def test():
    print(generate(0))
    print(generate(1))
    print(generate(2))
    print(generate(3))
    print(generate(4))


test()
