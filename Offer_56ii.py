""" 
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
剑指 Offer 56 - II. 数组中数字出现的次数 II
"""

from typing import List
import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = collections.Counter(nums)

        for k, v in res.items():
            if v == 1:
                return k
