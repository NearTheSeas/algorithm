""" 
https://leetcode-cn.com/problems/koko-eating-bananas/
875. 爱吃香蕉的珂珂

搜索左侧边界的二分
"""
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            return sum(math.ceil(p/k) for p in piles) <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not possible(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
