""" 
https://leetcode-cn.com/problems/XagZNi/
剑指 Offer II 037. 小行星碰撞
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for item in asteroids:
            while stack and stack[-1] > 0 and stack[-1] < -item:
                stack.pop()
            if stack and item < 0 and stack[-1] == -item:
                stack.pop()
            elif item > 0 or not stack or stack[-1] < 0:
                stack.append(item)
        return stack
