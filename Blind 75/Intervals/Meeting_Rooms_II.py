from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        meeting_rooms = []
        import heapq
        for interval in intervals:
            
            if meeting_rooms and meeting_rooms[0] <= interval.start:
                heapq.heappop(meeting_rooms)
            
            heapq.heappush(meeting_rooms, interval.end)
        return len(meeting_rooms)
