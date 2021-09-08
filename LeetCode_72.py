""" 
https://leetcode-cn.com/problems/edit-distance/
72. 编辑距离

dp[i][j]
    如果当前字符串相等，则直接跳过，
    如果不相等，则选取 删除i，删除j，或者替换操作中，最小的值 + 1
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m*n == 0:
            return m+n
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[m][n]
