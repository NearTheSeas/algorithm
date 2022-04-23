""" 
https://leetcode-cn.com/problems/jBjn9C/
剑指 Offer II 059. 数据流的第 K 大数值
"""
from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            heapq.heappush(self.minHeap, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
