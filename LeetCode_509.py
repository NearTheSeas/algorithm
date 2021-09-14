""" 
https://leetcode-cn.com/problems/fibonacci-number/
509. 斐波那契数
"""


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        p, q, r = 0, 0, 1
        for _ in range(2, n+1):
            p, q = q, r
            r = p + q
        return r
