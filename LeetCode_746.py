""" 
https://leetcode-cn.com/problems/min-cost-climbing-stairs/
746. 使用最小花费爬楼梯

数组cost的长度为n，则n个阶梯分别对应下标0到n−1，楼层顶部对应下标n，
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[n]
