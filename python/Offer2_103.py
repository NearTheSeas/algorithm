""" 
https://leetcode-cn.com/problems/gaM7Ch/
剑指 Offer II 103. 最少的硬币数目
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != amount+1 else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            num = coins[i-1]
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                if j >= num:
                    dp[i][j] += dp[i-1][j-num]
        return dp[-1][-1]
