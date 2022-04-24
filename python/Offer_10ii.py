""" 
https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
剑指 Offer 10- II. 青蛙跳台阶问题
"""


class Solution:
    def numWays(self, n: int) -> int:
        p, q = 1, 1
        for _ in range(n):
            p, q = q, p+q
        return p % 1000000007
