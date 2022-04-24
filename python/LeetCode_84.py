""" 
https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积
单调栈
"""
from types import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        # 增加左右哨兵
        heights = [0] + heights + [0]
        stack = [0]
        n += 2
        for i in range(n):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, width*height)
            stack.append(i)
        return ans

    def largestRectangleArea2(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        for i in range(n):
            height = heights[i]
            left, right = i, i
            while left - 1 >= 0 and heights[left-1] >= height:
                left -= 1
            while right + 1 <= n-1 and heights[right+1] >= height:
                right += 1
            ans = max(ans, (right-left+1)*height)
        return ans
