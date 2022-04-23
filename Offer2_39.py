""" 
https://leetcode-cn.com/problems/0ynMMM/
剑指 Offer II 039. 直方图最大矩形面积
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0
        for i, cur in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= cur:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(height * width, ans)
            stack.append(i)
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            ans = max(height * width, ans)
        return ans
