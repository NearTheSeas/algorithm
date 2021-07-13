"""
https://leetcode-cn.com/problems/decode-ways/
91. 解码方法
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n # 空字符串有一种解码方法
        for i in range(1, n+1):
            # i 从1开始的，所以对比的字符串是 是s[i-1] s[i-2]
            if s[i - 1] != '0':
                dp[i] += dp[i-1]
            if i > 1 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]
