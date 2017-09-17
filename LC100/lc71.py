"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together,
 such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""


def simplify(path):
    dirs = [p for p in path.split("/") if p != "" and p != "."]
    stack = []
    for p in dirs:
        if p == "..":
            if stack:
                stack.pop()
        else:
            stack.append(p)

    return "/" + "/".join(stack)


def test():
    path_list = [
        "",
        "/",
        "/a/b/./../c/",
        "/home/a/../",
        "//",
        "/../"
    ]
    for path in path_list:
        print(simplify(path))


test()
