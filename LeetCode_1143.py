""" 
https://leetcode-cn.com/problems/longest-common-subsequence/
1143. 最长公共子序列

dp[i][j] 表示 text1[0:i] text2[0:j]的最长公共子序列长度
text1[0:i] 表示 text_1的长度为 i 的前缀，
text2[0:j] 表示 text_2的长度为 j 的前缀

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
