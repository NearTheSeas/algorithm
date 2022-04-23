""" 
https://leetcode-cn.com/problems/Gu0c2T/
剑指 Offer II 089. 房屋偷盗
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return max(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

    def rob4(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        prev_max = curr_max = 0

        for num in nums:
            tmp_max = max(curr_max, prev_max + num)
            prev_max, curr_max = curr_max, tmp_max

        return curr_max

