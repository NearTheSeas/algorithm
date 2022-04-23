""" 
https://leetcode-cn.com/problems/ZL6zAn/
剑指 Offer II 105. 岛屿的最大面积
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def helper(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            ans = 1
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                ans += helper(x, y)
            return ans

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(helper(i, j), res)
        return res
