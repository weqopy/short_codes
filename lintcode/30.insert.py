"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """

    def insert(self, intervals, newInterval):
        results = []
        insertPos = 0
        for interval in intervals:
            if interval[1] < newInterval[0]:
                results.append(interval)
                insertPos += 1
            elif interval[0] > newInterval[1]:
                results.append(interval)
            else:
                m = min(interval[0], newInterval[0])
                n = max(interval[1], newInterval[1])
                newInterval = tuple([m, n])
        results.insert(insertPos, newInterval)
        return results
