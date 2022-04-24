""" 
https://leetcode-cn.com/problems/ZVAVXX/
剑指 Offer II 009. 乘积小于 K 的子数组
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, window, ans = 0, 1, 0
        for right in range(len(nums)):
            window *= nums[right]
            while left <= right and window >= k:
                window /= nums[left]
                left += 1
            ans += right - left + 1 if right >= left else 0
        return ans
