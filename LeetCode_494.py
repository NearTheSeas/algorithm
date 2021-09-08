""" 
https://leetcode-cn.com/problems/target-sum/
494. 目标和
正项和 - 负项和 = target 
正项和 + 负项和 = sum(nums)
正项和 = (target + sum(nums)) / 2
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumAll = sum(nums)
        if target > sumAll or (target + sumAll) % 2:
            return 0
        if len(nums) == 1 and abs(nums[0] != abs(target)):
            return 0
        target = (target + sumAll) // 2

        dp = [0] * (target + 1)
        dp[0] = 1  # dp[j] 表示填满容量为j的背包，有dp[j]种方法
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]

        return dp[-1]
