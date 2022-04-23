""" 
https://leetcode-cn.com/problems/WGki4K/
剑指 Offer II 004. 只出现一次的数字 
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0]*32
        for num in nums:
            for j in range(32):
                # 从最后一位开始计算
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            # 前面从最后一位开始计算的，所以 31-i 来倒叙操作
            res |= counts[31 - i] % m
            # python 存储负数特殊性
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)
