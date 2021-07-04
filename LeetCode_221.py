""" 
https://leetcode-cn.com/problems/maximal-square/
221. 最大正方形

dp(i,j) 表示以 (i, j)(i,j) 为右下角，且只包含 11 的正方形的边长最大值
dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        rows, columns = len(matrix), len(matrix[0])
        if rows == 0 or columns == 0:
            return 0
        border = 0
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1],
                                       dp[i-1][j-1]) + 1
                    border = max(border, dp[i][j])
        return border**2
