""" 
https://leetcode-cn.com/problems/kLl5u1/
剑指 Offer II 006. 排序数组中两个数字之和
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp == target:
                return [left, right]
            elif tmp > target:
                right -= 1
            elif tmp < target:
                left += 1
