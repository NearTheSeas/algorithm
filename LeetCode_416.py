"""
https://leetcode-cn.com/problems/partition-equal-subset-sum/
416. 分割等和子集
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        target = sum(nums)
        maxNum = max(nums)
        if target & 1:
            return False

        target //= 2
        if maxNum > target:
            return False
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target+1):
                if j >= num:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-num]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][target]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False]*target
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j-num]

        return dp[target]
