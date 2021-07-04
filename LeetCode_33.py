""" 
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
33. 搜索旋转排序数组
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid == nums[mid]:
                return mid
            if nums[0] < nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
