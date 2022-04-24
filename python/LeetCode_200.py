""" 
https://leetcode-cn.com/problems/number-of-islands/
200. 岛屿数量

图遍历
并查集
"""
from typing import List


class UnionFind:
    def __init__(self, grid: List[List[str]]) -> None:
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1]*(m*n)
        self.rank = [0]*(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i*n+j] = i*n+j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


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

    def numIslands2(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        columns = len(grid[0])

        uf = UnionFind(grid)
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    for newRow, newCol in [(row - 1, col), (row, col+1), (row+1, col), (row, col-1)]:
                        if 0 <= newRow < rows and 0 <= newCol < columns and grid[newRow][newCol] == '1':
                            uf.union(row*columns + col,
                                     newRow*columns + newCol)
        return uf.getCount()
