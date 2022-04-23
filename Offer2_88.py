""" 
https://leetcode-cn.com/problems/GzCJIP/
剑指 Offer II 088. 爬楼梯的最少成本
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-1])
        return dp[-1]

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n = len(cost)
        prev = curr = 0
        for i in range(2, n + 1):
            prev, curr = curr,  min(curr + cost[i - 1], prev + cost[i - 2])

        return curr
