""" 
https://leetcode-cn.com/problems/reverse-bits/
190. 颠倒二进制位
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)  # 取得n的最低位 翻转 赋给res res左移
            n >>= 1  # n右移
        return res
