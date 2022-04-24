""" 
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
121. 买卖股票的最佳时机
只能在某一天买入
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo, profix = float('inf'), 0
        for price in prices:
            lo = min(lo, price)
            profix = max(profix, price - lo)
        return profix
