""" 
https://leetcode-cn.com/problems/power-of-two/
231. 2 的幂

一个数 nn 是 22 的幂，当且仅当 nn 是正整数，并且 nn 的二进制表示中仅包含 11 个 11
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & -n) == n
