""" 
https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
剑指 Offer 53 - I. 在排序数组中查找数字 I

有序数组 二分法找左右边界
    1) 两个循环 分别找左右边界
    2) helper 找右边界 分别找target和target-1的右边界
"""
from typing import List
import collections


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return 0
        i, j = 0, len(nums)-1
        while i <= j:
            m = i+(j-i) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i
        i = 0
        while i <= j:
            m = i+(j-i) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j
        return right - left - 1

    def search(self, nums: List[int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i
        return helper(target) - helper(target - 1)

    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return 0
        counters = collections.Counter(nums)
        return counters[target]