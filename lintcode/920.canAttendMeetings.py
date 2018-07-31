"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        if len(intervals) == 0:
            return True

        intervals = sorted(intervals, key=lambda x: x.start)

        end = intervals[0].end
        for i in range(1, len(intervals)):
            if end > intervals[i].start:
                return False
            end = intervals[i].end
        return True
