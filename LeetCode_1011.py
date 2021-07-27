""" 
https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/
1011. 在 D 天内送达包裹的能力
"""
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo+hi) // 2
            d = self.countDays(mid, weights)
            if d > days:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def countDays(self, targetWeight, weights):
        days = 1
        current = 0
        for weight in weights:
            current += weight
            if current > targetWeight:
                days += 1
                current = weight
        return days
