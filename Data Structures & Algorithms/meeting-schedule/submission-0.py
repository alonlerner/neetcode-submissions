
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        d = defaultdict(bool)
        for i in intervals:
            for j in range(i.start, i.end):
                if d[j]: return False
                d[j] = True
        return True