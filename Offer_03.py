""" 
https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
剑指 Offer 03. 数组中重复的数字
"""
import collections
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        for num in nums:
            if dic[num] >= 1:
                return num
            dic[num] += 1
        return -1
