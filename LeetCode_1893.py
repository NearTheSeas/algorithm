""" 
https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered/
1893. 检查是否区域内所有整数都被覆盖
"""

from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1

        cur = 0
        for i in range(1, 51):
            cur += diff[i]
            if left <= i <= right and cur <= 0:
                return False
        return True
