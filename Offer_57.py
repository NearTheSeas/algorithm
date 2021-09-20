""" 
https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
剑指 Offer 57. 和为s的两个数字
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l <= r:
            val = nums[l]+nums[r]
            if val < target:
                l += 1
            if val > target:
                r -= 1
            if val == target:
                return [nums[l], nums[r]]
