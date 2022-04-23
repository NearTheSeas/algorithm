""" 
https://leetcode-cn.com/problems/7p8L0Z/
剑指 Offer II 084. 含有重复元素集合的全排列 
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(idx):
            if idx == len(nums):
                res.append(nums[:])
                return
            visited = set()
            for i in range(idx, len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    nums[idx], nums[i] = nums[i], nums[idx]
                    helper(idx + 1)
                    nums[idx], nums[i] = nums[i], nums[idx]
        helper(0)
        return res
