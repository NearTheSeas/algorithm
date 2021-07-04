""" 
https://leetcode-cn.com/problems/coin-change/
322. 零钱兑换
回溯的方法枚举每个硬币数量子集 会超时，需优化
增加了测试用例，贪心并不合适了
[186,419,83,408]
6249
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
