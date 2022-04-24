""" 
https://leetcode-cn.com/problems/PLYXKQ/
剑指 Offer II 040. 矩阵中最大的矩形
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights, ans = [0] * n, 0
        for row in matrix:
            for i in range(n):
                if row[i] == '0':
                    heights[i] = 0
                else:
                    heights[i] += 1
            ans = max(ans, self.largestArea(heights))
        return ans

    def largestArea(self, heights: List[int]) -> int:
        stack, ans = [-1], 0

        for i, cur in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= cur:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)

        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            ans = max(ans, height * width)
        return ans
