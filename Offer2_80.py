""" 
https://leetcode-cn.com/problems/uUsW3B/
剑指 Offer II 080. 含有 k 个元素的组合
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = list(range(1, n+1))

        def helper(idx, path):
            if len(path) == k:
                res.append(path[:])
            for i in range(idx, len(nums)):
                path.append(nums[i])
                helper(i+1, path)
                path.pop()

        helper(0, [])
        return res
