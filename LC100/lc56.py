"""
Merge Interval
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


def merge(intervals):
    output = []
    intervals.sort(key=lambda i: i.start)
    for an_interval in intervals:
        if output and an_interval.start <= output[-1].end:
            output[-1].end = max(an_interval.end, output[-1].end)
        else:
            output.append(intervals)

    return
