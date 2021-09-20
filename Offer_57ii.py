""" 
https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
剑指 Offer 57 - II. 和为s的连续正数序列
"""

from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, window, res = 1, 2, 3, []

        while i < j:
            if window == target:
                res.append(list(range(i, j+1)))
            if window > target:
                window -= i
                i += 1
            else:
                j += 1
                window += j
        return res
