""" 
https://leetcode-cn.com/problems/longest-common-subsequence/
1143. 最长公共子序列

dp[i][j] 表示 text1 和 text2的长度，所以范围是[0,m+1]  [0,n+1]
i j从1开始是因为字符串下标从0开始 取0的情况 是边界值
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
