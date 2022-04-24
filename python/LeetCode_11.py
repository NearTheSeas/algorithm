""" 
https://leetcode-cn.com/problems/container-with-most-water/

desc:盛水最多的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

input: hights 
output: max area

key: 左右双指针向中间收敛
"""

from typing import List


def maxArea(height: List[int]) -> int:
    if not height:
        return 0

    result = 0
    left, right = 0, len(height)-1
    while(left < right):
        area = (right - left) * min(height[left], height[right])
        result = max(result, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result
