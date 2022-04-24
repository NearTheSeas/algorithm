""" 
https://leetcode-cn.com/problems/IlPe0q/
剑指 Offer II 100. 三角形中最小路径之和
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        res = triangle[-1]
        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                res[col] = min(res[col], res[col+1]) + triangle[row][col]
        return res[0]
