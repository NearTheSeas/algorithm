""" 
https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
剑指 Offer 63. 股票的最大利润
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        ans = 0
        for num in prices:
            low = min(num, low)
            ans = max(num-low, ans)
        return ans
