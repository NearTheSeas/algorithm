""" 
https://leetcode-cn.com/problems/2bCMpM/
剑指 Offer II 107. 矩阵中的距离
"""
from typing import List
import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[m+n]*n for _ in range(m)]
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            dist = dp[x][y]
            for _x, _y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= _x < m and 0 <= _y < n:
                    if dp[_x][_y] > dist+1:
                        dp[_x][_y] = dist+1
                        q.append((_x, _y))
        return dp
