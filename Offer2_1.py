""" 
https://leetcode-cn.com/problems/xoh6Oh/
剑指 Offer II 001. 整数除法
"""


class Solution:
    def divide(self, a: int, b: int) -> int:
        INF_MIN, INF_MAX = -2**31, 2**31 - 1
        # 负数的最小值转换为正数会导致溢出
        if a == INF_MIN and b == -1:
            return INF_MAX

        negative = 2
        if a > 0:
            negative -= 1
            a = -a
        if b > 0:
            negative -= 1
            b = -b

        res = 0
        # a, b都转为了负数 
        while a <= b:
            value = b
            counter = 1
            # value * 2 不会超过最小值 且 value*2 不会超过 a
            while value >= (INF_MIN / 2) and a <= (value + value):
                counter += counter
                value += value
            res += counter
            a -= value

        return -res if negative == 1 else res
