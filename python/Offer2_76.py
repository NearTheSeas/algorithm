""" 
https://leetcode-cn.com/problems/xx4gT2/
剑指 Offer II 076. 数组中的第 k 大的数字
"""

from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1
        idx = self.partition(nums, left, right)
        while idx != target:
            if idx > target:
                right = idx - 1
            else:
                left = idx + 1
            idx = self.partition(nums, left, right)
        return nums[idx]

    def partition(self, nums, left, right):
        begin = random.randint(left, right)
        nums[left], nums[begin] = nums[begin], nums[left]
        pivot = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[i] = nums[i], nums[left]
        return i
