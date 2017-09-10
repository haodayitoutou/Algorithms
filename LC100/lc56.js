class interval {
    constructor(start=0, end=0) {
        this.start = start;
        this.end = end;
    }
}

function merge(intervals) {
    var output = [];
    intervals.sort( (a, b) => {
        return a.start - b.start;
    });

    var last;
    for (var an_interval of intervals) {
        if (output.length > 0 && an_interval.start <= last.end) {
            last.end = Math.max(an_interval.end, last.end);
        } else {
            output.push(an_interval);
            last = an_interval;
        }
    }
    return output;
}


var intervals = [
    new interval(1, 3),
    new interval(2, 6),
    new interval(8, 10),
    new interval(15, 18),
];
merge(intervals);
