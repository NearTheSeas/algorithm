"""
https://leetcode-cn.com/problems/unique-paths-ii/
63. 不同路径 II
初始dp就得考虑障碍物情况
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        # 第一个格子可能有障碍物
        dp[0][0] = 0 if obstacleGrid[0][0] else 1

        # 处理第一列
        for i in range(1, m):
            # 当前行的当前一列有障碍物 或者 前一行过来的值是0
            if obstacleGrid[i][0] or dp[i-1][0] == 0:
                dp[i][0] = 0
            else:
                dp[i][0] = 1
        # 处理第一行
        for i in range(1, n):
            # 当前列有障碍物 或者 前一个格传递过来的是0
            if obstacleGrid[0][i] or dp[0][i-1] == 0:
                dp[0][i] = 0
            else:
                dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                # 如果有障碍 则值为0
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
