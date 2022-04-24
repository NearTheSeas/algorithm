""" 
https://leetcode-cn.com/problems/tvdfij/
剑指 Offer II 012. 左右两边子数组的和相等
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        preSum = 0
        for i, num in enumerate(nums):
            preSum += num
            if preSum - num == total - preSum:
                return i
        return -1
