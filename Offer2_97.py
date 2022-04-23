""" 
https://leetcode-cn.com/problems/21dk04/
剑指 Offer II 097. 子序列的数目
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 1
        for i in range(1, m+1):
            dp[i][0] = 1
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
