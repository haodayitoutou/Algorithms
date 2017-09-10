class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }
}

function insert_interval(intervals, new_interval) {
    var left = [], right = [];
    var start = new_interval.start;
    var end = new_interval.end;
    for (var inter of intervals) {
        if (inter.end < start) {
            left.push(inter);
        } else if (inter.start > end) {
            right.push(inter);
        } else {
            start = Math.min(start, inter.start);
            end = Math.max(end, inter.end);
        }
    }

    return left + [Interval(start, end)] + right;
}