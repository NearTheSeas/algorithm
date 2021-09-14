"""
https://leetcode-cn.com/problems/super-pow/
372. 超级次方
"""
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        base = 1337
        for i in b:
            res = self.qpow(res, 10, base) * self.qpow(a, i, base)
        return res % base

    def qpow(self, x, n, base):
        ans = 1
        x %= base
        while n > 0:
            if n & 1 == 1:
                ans = ans * x % base
            x = x * x % base
            n >>= 1
        return ans
