""" 
https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/
剑指 Offer 59 - II. 队列的最大值
"""


class MaxQueue:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def max_value(self) -> int:
        return self.max_stack[0] if self.max_stack else -1

    def push_back(self, value: int) -> None:
        self.stack.append(value)
        while self.max_stack and self.max_stack[-1] < value:
            self.max_stack.pop()
        self.max_stack.append(value)

    def pop_front(self) -> int:
        if not self.stack:
            return -1
        removed = self.stack.pop(0)
        if removed == self.max_stack[0]:
            self.max_stack.pop(0)
        return removed

        # Your MaxQueue object will be instantiated and called as such:
        # obj = MaxQueue()
        # param_1 = obj.max_value()
        # obj.push_back(value)
        # param_3 = obj.pop_front()
