""" 
https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
剑指 Offer 10- I. 斐波那契数列
转移方程： dp[i+1] = dp[i] + dp[i-1] 
即对应数列定义 f(n + 1) = f(n) + f(n - 1)

初始状态 dp[0]=1 dp[1] =1 
返回值 dp[n]
"""


class Solution:
    def fib(self, n: int) -> int:
        p, q = 0, 1
        for _ in range(n):
            p, q = q, p + q
        return p % 1000000007
