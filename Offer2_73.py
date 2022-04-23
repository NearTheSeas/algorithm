""" 
https://leetcode-cn.com/problems/nZZqjQ/
剑指 Offer II 073. 狒狒吃香蕉
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if self.getHours(piles, mid) <= h:
                if mid == 1 or self.getHours(piles, mid-1) > h:
                    return mid
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def getHours(self, piles, speed):
        hour = 0
        for pile in piles:
            hour += (pile + speed - 1) // speed
        return hour
