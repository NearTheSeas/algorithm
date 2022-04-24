""" 
https://leetcode-cn.com/problems/distinct-subsequences/
115. 不同的子序列

dp[i][j] 表示 t[i:]
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]
