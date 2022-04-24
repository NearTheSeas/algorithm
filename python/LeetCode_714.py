"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
714. 买卖股票的最佳时机含手续费
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n-1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

    def maxProfit2(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(
                sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell
