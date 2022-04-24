""" 
https://leetcode-cn.com/problems/qIsx9U/
剑指 Offer II 041. 滑动窗口的平均值
"""


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.capacity = size
        self.amount = 0

    def next(self, val: int) -> float:
        if self.capacity == len(self.nums):
            removed = self.nums.pop(0)
            self.amount -= removed
        self.nums.append(val)
        self.amount += val

        return self.amount / len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
