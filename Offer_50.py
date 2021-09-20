""" 
https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
剑指 Offer 50. 第一个只出现一次的字符
"""
from typing import Collection


import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.defaultdict(int)

        for ch in s:
            dic[ch] += 1
        for ch in s:
            if dic[ch] == 1:
                return ch
        return ' '
