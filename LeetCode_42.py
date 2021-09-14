""" 
https://leetcode-cn.com/problems/trapping-rain-water/
接雨水 

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
