"""
https://leetcode-cn.com/problems/YaVDxD/
剑指 Offer II 102. 加减的目标值
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = sum(nums)

        if (target+sums) & 1 or sums < target:
            return 0
        if len(nums) == 1 and abs(nums[0]) != abs(target):
            return 0
        target = (sums + target) // 2
        dp = [0]*(target+1)
        dp[0] = 1
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] += dp[j-num]
        return dp[-1]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = sum(nums)

        if (target+sums) & 1 or sums < target:
            return 0
        if len(nums) == 1 and abs(nums[0]) != abs(target):
            return 0
        target = (sums + target) // 2
        dp = [[0]*(target+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = 1

        for i in range(1, len(nums)+1):
            num = nums[i-1]
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if j >= num:
                    dp[i][j] += dp[i-1][j-num]
        return dp[-1][-1]
