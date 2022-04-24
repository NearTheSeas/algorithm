""" 
https://leetcode-cn.com/problems/4sjJUc/
剑指 Offer II 082. 含有重复元素集合的组合
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(i, subset, target):
            if target <= 0 or i == len(candidates):
                if target == 0:
                    res.append(subset[:])
                return

            for j in range(i, len(candidates)):
                if i < j and candidates[j - 1] == candidates[j]:
                    continue
                subset.append(candidates[j])
                helper(j+1, subset, target - candidates[j])
                subset.pop()

        helper(0, [], target)
        return res
