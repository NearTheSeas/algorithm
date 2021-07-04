""" 
https://leetcode-cn.com/problems/number-of-islands/
200. 岛屿数量

图遍历
并查集
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            if not inArea(row, col):
                return
            if grid[row][col] != '1':
                return
            grid[row][col] = '2'

            # 遍历上下左右4个方向的邻居
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        # 判断是否在范围内
        def inArea(row, col):
            return row >= 0 and row < m and col >= 0 and col < n

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    counter += 1
                    dfs(row, col)
        return counter
