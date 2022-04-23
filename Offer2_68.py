""" 
https://leetcode-cn.com/problems/N6YdxV/
剑指 Offer II 068. 查找插入位置
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                right = mid - 1
            else:
                left = mid + 1
        return len(nums)
