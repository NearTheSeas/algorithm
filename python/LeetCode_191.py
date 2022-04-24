""" 
https://leetcode-cn.com/problems/number-of-1-bits/
191. 位1的个数

n & (n−1)，其运算结果恰为把 nn 的二进制位中的最低位的 11 变为 00 之后的结果
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n:
            n = n & (n-1)
            counter += 1
        return counter
