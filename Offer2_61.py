""" 
https://leetcode-cn.com/problems/qn8gGX/
剑指 Offer II 061. 和最小的 k 个数对
"""

from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []

        def push(i, j):
            if i < k and j < k:
                heapq.heappush(minHeap, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        res = []
        while minHeap and len(res) < k:
            _, i, j = heapq.heappop(minHeap)
            res.append([nums1[i], nums2[j]])
            push(i, j+1)
            if j == 0:
                push(i+1, 0)
        return res
