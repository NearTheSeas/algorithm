""" 
https://leetcode-cn.com/problems/omKAoA/
剑指 Offer II 094. 最少回文分割
"""


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        isPal = [[False]*n for _ in range(n)]
        for i in range(n):
            isPal[i][i] = True
            for j in range(i):
                if s[i] == s[j]:
                    if j+1 == i:
                        isPal[j][i] = True
                    else:
                        isPal[j][i] = isPal[j+1][i-1]

        dp = [n for _ in range(n)]
        for i in range(n):
            # s[0:i+1] 是回文
            if isPal[0][i]:
                dp[i] = 0
            else:
                # s[0:i+1] 不是回文
                # 在他前面找最小分割数 
                for j in range(i):
                    if isPal[j+1][i]:
                        dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]
