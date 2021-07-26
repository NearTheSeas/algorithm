""" 
https://leetcode-cn.com/problems/burst-balloons/
312. 戳气球

算法小抄思路
分数与相邻气球的分数有关，增加哨兵nums[-1]=nums[n]=1
dp[i][j] 戳破i,j之间的气球获得的分数
倒叙遍历 最后一个戳破的气球
dp[i][j] = dp[i][k] + dp[k][j] + points[i]*points[k]*points[j]

思路二
dp[i][j] 在开区间(i,j)之间插入气球 k，把区间分为了 dp[i][k]+dp[k][j]
"""
from typing import List
from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        points = [1] + nums + [1]
        # nums前后补1，长度为n+2
        dp = [[0]*(n+2) for _ in range(n+2)]
        for i in range(n, -1, -1):  # i取值范围n到0，j取值范围i+1,n+1,k取值 ij之间
            for j in range(i+1, n+2):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k]
                                   [j] + points[i]*points[j]*points[k])
        return dp[0][n+1]

    def maxCoins2(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]

        @lru_cache(None)
        def solve(left: int, right: int) -> int:
            if left >= right:
                return 0

            best = 0
            for i in range(left+1, right):
                total = val[left]*val[i]*val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
        return solve(0, n+1)
