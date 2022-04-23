""" 
https://leetcode-cn.com/problems/NUPfPr/
剑指 Offer II 101. 分割等和子集
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, target, maxVal = len(nums), sum(nums), max(nums)
        if n < 2 or target & 1:
            return False
        target = target >> 1
        if maxVal > target:
            return False
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        for i in range(1, n):
            num = nums[i]
            # nums 未排序，所以从 1 开始遍历
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num and not dp[i][j]:
                    dp[i][j] = dp[i - 1][j - num]
        return dp[-1][-1]

    def canPartition(self, nums: List[int]) -> bool:
        n, target, maxVal = len(nums), sum(nums), max(nums)
        if n < 2 or target & 1:
            return False
        target = target >> 1
        if maxVal > target:
            return False
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num-1, -1):
                if dp[target-i]:
                    dp[i] = True
        return dp[target]
