""" 
https://leetcode-cn.com/problems/subsets/
78. 子集

全排列 回溯
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + sub for sub in res]
        return res
