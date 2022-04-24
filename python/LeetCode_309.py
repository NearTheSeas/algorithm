""" 
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
309. 最佳买卖股票时机含冷冻期
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-prices[0], 0, 0]] + [[0]*3 for _ in range(n-1)]
        for i in range(1, n):
            # f[i][0]: 手上持有股票的最大收益
            # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
            # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[n-1][1], dp[n-1][2])
