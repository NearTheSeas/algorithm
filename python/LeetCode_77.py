""" 
https://leetcode-cn.com/problems/combinations/
77. 组合
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, track = [], []
        self.backtrack(n, k, 1, track, res)
        return res

    def backtrack(self, n, k, i, track, res):
        if len(track) == k:
            res.append(track[:])

        for j in range(i, n+1):
            track.append(j)
            self.backtrack(n, k, j+1, track, res)
            track.pop()
