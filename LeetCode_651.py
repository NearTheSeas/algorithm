""" 
https://leetcode-cn.com/problems/4-keys-keyboard/
651. 四键键盘
A
Ctrl + A 
Ctrl + C 
Ctrl + V
4种操作，获得最多的A
"""


class Solution:
    def maxA(self, n: int) -> int:
        memo = dict()

        def dp(n, a_num, copy):
            if n <= 0:
                return a_num
            if (n, a_num, copy) in memo:
                return memo[(n, a_num, copy)]
            memo[(n, a_num, copy)] = max(
                dp(n-1, a_num+1, dp(n-1, a_num+copy), dp(n-2, a_num, a_num)))
            return memo[(n, a_num, copy)]

        return dp(n, 0, 0)

    def maxA2(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            for j in range(2, i):
                dp[i] = max(dp[i], dp[j-2] * (i-j+1))
        return dp[-1]
