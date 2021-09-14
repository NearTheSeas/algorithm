""" 
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
34. 在排序数组中查找元素的第一个和最后一个位置
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]

        def binarySearch(is_left):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    if is_left:
                        while mid > 0 and nums[mid - 1] == target:
                            mid -= 1
                        return mid
                    else:
                        while mid < len(nums) - 1 and nums[mid + 1] == target:
                            mid += 1
                        return mid
            return -1

        return [binarySearch(True), binarySearch(False)]
