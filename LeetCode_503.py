""" 
https://leetcode-cn.com/problems/next-greater-element-ii/
503. 下一个更大元素 II
循环数组
"""
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        for i in range(n*2):
            real_i = i % n
            while stack and nums[stack[-1]] < nums[real_i]:
                res[stack.pop()] = nums[real_i]
            stack.append(real_i)
        return res
