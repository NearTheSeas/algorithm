""" 
https://leetcode-cn.com/problems/B1IidL/
剑指 Offer II 069. 山峰数组的顶部
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            if arr[mid - 1] < arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return 
