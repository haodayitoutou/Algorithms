function simplify(path) {
    var dirs, p, stack = [];
    dirs = path.split("/");
    for (p of dirs) {
        if (p === "..") {
            if (stack.length > 0) {
                stack.pop();
            }
        } else if (p === "." || p === "") {
            
        } else {
            stack.push(p);
        }
    }
    return "/" + stack.join("/");
}


function test() {
    var path_list = [
        "/a/b/./../c/",
        "/home/a/../",
        "",
        "/",
        "//",
        "/../"
    ];
    for (var path of path_list) {
        console.log(simplify(path));
    }
}


test();
