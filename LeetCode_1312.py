""" 
https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
1312. 让字符串成为回文串的最少插入次数
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][-1]

    def minInsertions2(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        for i in range(n-1, -1, -1):
            pre = 0
            for j in range(i+1, n):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j], dp[j-1]) + 1
                pre = tmp
        return dp[-1]
