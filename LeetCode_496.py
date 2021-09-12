""" 
https://leetcode-cn.com/problems/next-greater-element-i/
496. 下一个更大元素 I
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res_dict = {i: -1 for i in nums2}
        for i in nums2:
            while stack and i > stack[-1]:
                small = stack.pop()
                res_dict[small] = i
            stack.append(i)
        res = []
        for j in nums1:
            res.append(res_dict[j])
        return res
