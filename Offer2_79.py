"""
https://leetcode-cn.com/problems/TVdhkn/
剑指 Offer II 079. 所有子集
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)

        def helper(idx,  subset):
            res.append(subset[:])
            for i in range(idx, n):
                subset.append(nums[i])
                helper(i + 1, subset)
                subset.pop()

        helper(0, [])
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = []
        for num in nums:
            res = res + [[num] + sub for sub in res]
        return res

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(idx,  subset):
            if idx == len(nums):
                res.append(subset)
                return
            else:
                helper(idx+1, subset)
                subset.append(nums[idx])
                helper(idx+1, subset)
                subset.pop()

        return res
