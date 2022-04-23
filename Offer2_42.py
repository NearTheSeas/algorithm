""" 
https://leetcode-cn.com/problems/H8086Q/
剑指 Offer II 042. 最近请求次数
"""


class RecentCounter:

    def __init__(self):
        self.times = []
        self.capacity = 3000

    def ping(self, t: int) -> int:
        self.times.append(t)
        while self.times[0] + self.capacity < t:
            self.times.pop(0)
        return len(self.times)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
