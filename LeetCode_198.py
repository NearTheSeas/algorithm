""" 
https://leetcode-cn.com/problems/house-robber/
198. 打家劫舍
间隔取值
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[n-1]

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first+nums[i], second)
        return second
