""" 
https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
剑指 Offer 66. 构建乘积数组

dp[i] 前i-1个数的乘积  * 从右侧累乘到i+1位置
"""
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        dp = [1]*len(a)
        tmp = 1
        for i in range(1, len(a)):
            dp[i] = dp[i-1]*a[i-1]
        for i in range(len(a)-2, -1, -1):
            tmp *= a[i+1]
            dp[i] *= tmp
        return dp
