""" 
https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
167. 两数之和 II - 输入有序数组
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left+1, right+1]
        return []
