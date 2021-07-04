""" 
https://leetcode-cn.com/problems/coin-change-2/
518. 零钱兑换 II

https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-iihe-pa-lou-ti-wen-ti-dao-di-yo/
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        return dp[-1]
