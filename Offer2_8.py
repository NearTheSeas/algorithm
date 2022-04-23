""" 
https://leetcode-cn.com/problems/2VG8Kg/
剑指 Offer II 008. 和大于等于 target 的最短子数组
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, window, ans = 0, 0, len(nums) + 1
        for right in range(len(nums)):
            window += nums[right]
            while left <= right and window >= target:
                ans = min(ans, right - left + 1)
                window -= nums[left]
                left += 1
        return 0 if ans == len(nums) + 1 else ans
