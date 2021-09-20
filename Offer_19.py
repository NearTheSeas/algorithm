""" 
https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/
剑指 Offer 19. 正则表达式匹配

dp[i][j] 代表 s[:i] 与 p[:j] 是否可以匹配
dp[i][j] 对应的添加字符是 s[i - 1] 和 p[j - 1]


dp[i][j] = dp[i - 1][j - 2] && (s[i - 1] == p[j - 2])
而 dp[i - 1][j - 2] = dp[i - 1][j]，相对于 dp[i - 1][j - 2] 来说，这里的 *(也就是 p[j - 1]) 匹配了 0 次
两者合并即为：dp[i][j] = (dp[i - 1][j]) && (s[i - 1] == p[j - 2])

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(2, n+1, 2):
            dp[0][j] = dp[0][j-2] and p[j-1] == '*'
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    if dp[i][j-2]:
                        dp[i][j] = True
                    elif dp[i-1][j] and s[i-1] == p[j-2]:
                        dp[i][j] = True
                    elif dp[i-1][j] and p[j-2] == '.':
                        dp[i][j] = True
                else:
                    if dp[i-1][j-1] and s[i-1] == p[j-1]:
                        dp[i][j] = True
                    elif dp[i-1][j-1] and p[j-1] == '.':
                        dp[i][j] = True
        return dp[-1][-1]
