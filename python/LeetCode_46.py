""" 
https://leetcode-cn.com/problems/permutations/
46. 全排列
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        track, res = [], []
        self.backtrack(nums, track, res)
        return res

    def backtrack(self, nums, track, res):
        if len(track) == len(nums):
            res.append(track[:])
            return
        for num in nums:
            if num in track:
                continue
            track.append(num)
            self.backtrack(nums, track, res)
            track.pop()
