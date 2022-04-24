""" 
https://leetcode-cn.com/problems/Ygoe9J/
剑指 Offer II 081. 允许重复选择元素的组合
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(i, subset, target):
            if i >= len(candidates) or target < 0:
                return
            if target == 0:
                res.append(subset[:])
                return
            for j in range(i, len(candidates)):
                subset.append(candidates[j])
                # j 不增加，target减小 相当于重复选择一次
                helper(j, subset, target - candidates[j])
                subset.pop()

        helper(0, [], target)
        return res
