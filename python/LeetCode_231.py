""" 
https://leetcode-cn.com/problems/power-of-two/
231. 2 的幂

一个数 n 是 2 的幂，当且仅当 n 是正整数，并且 n 的二进制表示中仅包含 1 个 1
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & -n) == n
