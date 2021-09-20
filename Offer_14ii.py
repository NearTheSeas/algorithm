""" 
https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/
剑指 Offer 14- II. 剪绳子 II
"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n-1
        res = 1
        while n > 4:
            res = res * 3 % 1000000007
            n -= 3
        return res*n % 1000000007
