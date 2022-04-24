""" 
https://leetcode-cn.com/problems/iIQa4I/
剑指 Offer II 038. 每日温度
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stack = [0]*len(temperatures), []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res
