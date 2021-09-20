"""
https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
剑指 Offer 09. 用两个栈实现队列
"""


class CQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def appendTail(self, value: int) -> None:
        self.stackA.append(value)

    def deleteHead(self) -> int:
        if self.stackB:
            return self.stackB.pop()
        if not self.stackA:
            return -1

        while self.stackA:
            self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

        # Your CQueue object will be instantiated and called as such:
        # obj = CQueue()
        # obj.appendTail(value)
        # param_2 = obj.deleteHead()
