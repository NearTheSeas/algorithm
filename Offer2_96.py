""" 
https://leetcode-cn.com/problems/IY6buf/
剑指 Offer II 096. 字符串交织
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = s1[i-1] == s3[i-1] and dp[i-1][0]
        for j in range(1, n+1):
            dp[0][j] = s2[j-1] == s3[j-1] and dp[0][j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]
        return dp[-1][-1]
