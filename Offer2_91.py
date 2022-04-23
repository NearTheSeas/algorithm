""" 
https://leetcode-cn.com/problems/JEj789/
剑指 Offer II 091. 粉刷房子
"""
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[0]*3 for _ in range(len(costs))]
        dp[0] = costs[0]
        for i in range(1, len(costs)):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        return min(dp[-1])

    def minCost(self, costs: List[List[int]]) -> int:
        r = b = g = 0
        for x, y, z in costs:
            r, b, g = min(g, b) + x, min(r, g) + y, min(r, b) + z
        return min(r, g, b)
