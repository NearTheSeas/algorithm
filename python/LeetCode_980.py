""" 
https://leetcode-cn.com/problems/unique-paths-iii/
980. 不同路径 III

dfs 回溯
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.res = 0
        sr, sc, er, ec = 0, 0, 0, 0  # 起点 终点
        step = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    sr, sc = r, c
                if grid[r][c] == 2:
                    er, ec = r, c
                if grid[r][c] != -1:
                    step += 1
        def backtrack(r, c, step):
            step -= 1
            if r == er and c == ec:
                if step == 0:
                    self.res += 1
                return
            grid[r][c] = -1
            for nr, nc in ((r-1, c), (r, c+1), (r+1, c), (r, c-1)):
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    backtrack(nr, nc, step)
            grid[r][c] = 0

        backtrack(sr, sc, step)
        return self.res
