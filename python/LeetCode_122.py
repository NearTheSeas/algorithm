""" 
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
122. 买卖股票的最佳时机 II
可以买卖多次

每天的股票有两种持仓情况：
    0是前一天手里没有股票，
    1是前一天有股票
当天的股票收益
    今天不持有：前一天没有股票的情况 或 前一天有今天卖了
    今天持有：前一天有股票的情况下，今天的价格卖出或不卖
    
因为持有股票要花钱，所以当天如果买入 就是-price 卖出获得收益就是+price
"""

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0  # 不持有
        dp[0][1] = -float('inf')  # 持有
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])

        return dp[-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        curHold, curNotHold = -float('inf'), 0
        for stock in prices:
            curHold, curNotHold = max(
                curHold, curNotHold - stock), max(curNotHold, curHold + stock)
        return curNotHold if prices else 0
