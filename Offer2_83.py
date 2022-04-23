""" 
https://leetcode-cn.com/problems/VvJkup/
剑指 Offer II 083. 没有重复元素集合的全排列
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(idx):
            if idx == len(nums):
                res.append(nums[:])
                return

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                helper(idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]
        helper(0)
        return res
