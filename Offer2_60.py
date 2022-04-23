""" 
https://leetcode-cn.com/problems/g5c51o/
剑指 Offer II 060. 出现频率最高的 k 个数字
"""
from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = collections.Counter(nums)
        minHeap, res = [], []
        for num, count in num_count.items():
            if len(minHeap) == k:
                if minHeap[0][0] < count:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (count, num))
            else:
                heapq.heappush(minHeap, (count, num))
        while minHeap:
            count, num = heapq.heappop(minHeap)
            res.append(num)
        return res
