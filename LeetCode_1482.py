""" 
https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets/
1482. 制作 m 束花所需的最少天数

二分法遍历天数
"""
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m > len(bloomDay) / k:
            return -1

        def canMake(days: int) -> bool:
            bouquets = flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        if bouquets == m:
                            break
                        flowers = 0
                else:
                    flowers = 0
            return bouquets == m

        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            days = (lo + hi) // 2
            if canMake(days):
                hi = days
            else:
                lo = days+1
        return lo
