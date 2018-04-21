"""
给出若干闭合区间，合并所有重叠的部分。
"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self[0] = start
        self[1] = end
"""


# Use Interval
class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """

    def merge(self, intervals):
        n = len(intervals)
        if n < 2:
            return intervals
        result = []
        intervals.sort(key=lambda d: d.start)
        index = 1
        left, right = intervals[0].start, intervals[0].end
        while index < n:
            if intervals[index].start <= right:
                right = max(intervals[index].end, right)
            else:
                result.append(Interval(left, right))
                left = intervals[index].start
                right = intervals[index].end
            index += 1
        result.append(Interval(left, right))
        return result


class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """

    def merge(self, intervals):
        n = len(intervals)
        if n < 2:
            return intervals
        result = []
        intervals.sort(key=lambda d: d[0])
        index = 1
        left, right = intervals[0][0], intervals[0][1]
        while index < n:
            if intervals[index][0] <= right:
                right = max(intervals[index][1], right)
            else:
                result.append((left, right))
                left = intervals[index][0]
                right = intervals[index][1]
            index += 1
        result.append((left, right))
        return result


# i = [(1, 3), (2, 6), (8, 10), (15, 18)]
# print(Solution().merge(i))
