""" 
https://leetcode-cn.com/problems/1fGaJU/
剑指 Offer II 007. 数组中和为 0 的三个数
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) >= 3:
            nums.sort()
            i = 0
            while i < len(nums) - 2:
                self.twoSum(nums, i, res)
                tmp = nums[i]
                while i < len(nums) and nums[i] == tmp:
                    i += 1
        return res

    def twoSum(self, numbers: List[int],  start: int, res: List[int]) -> List[int]:
        left, right = start+1, len(numbers)-1
        while left < right:
            if numbers[start] + numbers[left] + numbers[right] == 0:
                res.append([numbers[start], numbers[left], numbers[right]])
                tmp = numbers[left]
                while numbers[left] == tmp and left < right:
                    left += 1
            elif numbers[start] + numbers[left] + numbers[right] < 0:
                left += 1
            else:
                right -= 1
