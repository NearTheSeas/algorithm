""" 
https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            while nums[left] & 1 == 1 and left < right:
                left += 1
            while nums[right] & 1 == 0 and left < right:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums

    def exchange(self, nums: List[int]) -> List[int]:
        low, fast = 0, 0
        while fast < len(nums):
            if fast & 1 == 1:
                nums[low], nums[fast] = nums[fast], nums[low]
                low += 1
            fast += 1
        return nums
