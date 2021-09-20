""" 
https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
剑指 Offer 53 - I. 在排序数组中查找数字 I
"""
from typing import List


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
