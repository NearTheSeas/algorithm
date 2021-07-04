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
        curHold, curNotHold = -float('inf'), 0

        for stock in prices:
            prevHold, preNotHold = curHold, curNotHold
            curHold = max(prevHold, preNotHold - stock)
            curNotHold = max(preNotHold, prevHold + stock)

        return curNotHold if prices else 0
