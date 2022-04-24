""" 
https://leetcode-cn.com/problems/triangle/
120. 三角形最小路径和

[2]
[3,4]
[6,5,7]
[4,1,8,3]


"""
from typing import List


class Solution:
    # 此方法不如从最后一行倒推
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            # dp每行第一个值没有其他选择 直接取自上一行第一个值 + 本行第一个值
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            # dp每行最后一个值同样没有其他选择 直接取自上一行最后一个值 + 当前值
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        return min(dp[n-1])

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
