""" 
https://leetcode-cn.com/problems/maximal-rectangle/
85. 最大矩形
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0]*(n+1)
        res = 0
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j]+1 if matrix[i][j] == '1' else 0

            stack = [-1]
            for k, num in enumerate(heights):
                while stack and num < heights[stack[-1]]:
                    index = stack.pop()
                    res = max(res, heights[index]*(k - stack[-1] - 1))
                stack.append(k)
        return res
