""" 
https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
剑指 Offer 17. 打印从1到最大的n位数

大数计算
"""

from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res

    def printNumbers(self, n: int) -> List[int]:
        def dfs(index, num, digit):
            if index == digit:
                res.append(int(''.join(num)))
                return
            for i in range(10):
                num.append(str(i))
                dfs(index+1, num, digit)
                num.pop()
        res = []
        for digit in range(1, n+1):
            for first in range(1, 10):
                num = [str(first)]
                dfs(1, num, digit)
        return res
