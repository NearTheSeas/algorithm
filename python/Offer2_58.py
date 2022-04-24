""" 
https://leetcode-cn.com/problems/fi9suh/
剑指 Offer II 058. 日程表
"""
from sortedcontainers import SortedDict


class MyCalendar:

    def __init__(self):
        self.end_start = SortedDict()

    def book(self, start: int, end: int) -> bool:
        ID = self.end_start.bisect_right(start)
        if 0 <= ID < len(self.end_start):
            if self.end_start.values()[ID] < end:
                return False
        self.end_start[end] = start
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
