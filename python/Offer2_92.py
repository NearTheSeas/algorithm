""" 
https://leetcode-cn.com/problems/cyJERH/
剑指 Offer II 092. 翻转字符
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0 if s[0] == '0' else 1
        dp[0][1] = 0 if s[0] == '1' else 1
        for i in range(1, n):
            if s[i] == '0':
                dp[i][0] = dp[i-1][0]
                dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = min(dp[i-1][0], dp[i-1][1])
        return min(dp[-1])
