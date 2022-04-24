""" 
https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
剑指 Offer 53 - II. 0～n-1中缺失的数字
"""
from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num != i:
                return i
        return len(nums)

    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i
