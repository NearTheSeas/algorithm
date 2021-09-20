""" 
https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
剑指 Offer 61. 扑克牌中的顺子
"""

from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        maxVal, minVal = 0, 14
        for num in nums:
            if num == 0:
                continue
            maxVal = max(maxVal, num)
            minVal = min(minVal, num)
            if num in repeat:
                return False
            repeat.add(num)
        return maxVal - minVal < 5
