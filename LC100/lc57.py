"""
Given a set of non-overlapping intervals,
insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted
according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16],
insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "Interval {}-{}".format(self.start, self.end)


def insert_interval(intervals, new_interval):
    left, right = [], []
    start, end = new_interval.start, new_interval.end
    for inter in intervals:
        if inter.end < start:
            left.append(inter)
        elif inter.start > end:
            right.append(inter)
        else:
            start = min(start, inter.start)
            end = max(end, inter.end)

    return left + [Interval(start, end)] + right


def test():
    intervals = [
        Interval(1, 2),
        Interval(3, 5),
        Interval(6, 7),
        Interval(8, 10),
        Interval(12, 16)
    ]
    new_interval = Interval(4, 9)
    print(
        insert_interval(intervals, new_interval)
    )

test()
