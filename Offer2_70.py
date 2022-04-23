""" 
https://leetcode-cn.com/problems/skFtm2/
剑指 Offer II 070. 排序数组中只出现一次的数字
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) // 2
        while left <= right:
            mid = left + (right - left) // 2
            i = mid * 2
            if i < len(nums)-1 and nums[i] != nums[i+1]:
                if mid == 0 or nums[i-2] == nums[i-1]:
                    return nums[i]
                right = mid - 1
            else:
                left = mid + 1
        return nums[-1]
