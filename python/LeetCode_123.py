""" 
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
123. 买卖股票的最佳时机 III

最多可以完成 两笔 交易
不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）

五个状态
未进行过任何操作；
只进行过一次买操作；
进行了一次买操作和一次卖操作，即完成了一笔交易；
在完成了一笔交易的前提下，进行了第二次买操作；
完成了全部两笔交易。

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2
