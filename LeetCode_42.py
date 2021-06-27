""" 
https://leetcode-cn.com/problems/trapping-rain-water/
接雨水 
desc:给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
input:height[int]
output:max
key: 动态规划 单调栈 双指针
"""
from typing import List


def trap(height: List[int]) -> int:
    left, right, ans = 0, len(height)-1, 0
    leftMax, rightMax = 0, 0
    while left < right:
        leftMax = max(leftMax, height[left])
        rightMax = max(rightMax, height[right])
        if leftMax < rightMax:
            ans += leftMax - height[left]
            left += 1
        else:
            ans += rightMax - height[right]
            right -= 1

    return ans
