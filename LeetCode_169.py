""" 
https://leetcode-cn.com/problems/majority-element/
169. 多数元素
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        majority = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] == majority:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    majority = nums[i]
                    counter = 1
        return majority
