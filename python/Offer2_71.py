""" 
https://leetcode-cn.com/problems/cuyjEf/
剑指 Offer II 071. 按权重生成随机数
"""
from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        self.preSums = [0]*len(w)
        self.total = 0
        for i, num in enumerate(w):
            self.total += num
            self.preSums[i] = self.total

    def pickIndex(self) -> int:
        p = random.randint(1, self.total)  # 随机的是权重范围 [1, total]
        print(p)
        left, right = 0, len(self.preSums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.preSums[mid] >= p:
                if mid == 0 or self.preSums[mid-1] < p:
                    return mid
                right = mid - 1
            else:
                left = mid + 1
        return -1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
