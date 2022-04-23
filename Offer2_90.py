""" 
https://leetcode-cn.com/problems/PzWKhm/
剑指 Offer II 090. 环形房屋偷盗
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            r1 = self.robRange(nums, 0, n-2)
            r2 = self.robRange(nums, 1, n-1)
            return max(r1, r2)

    def robRange(self, nums: List[int], start, end) -> int:
        prev, cur = nums[start], max(nums[start], nums[start+1])
        for i in range(start+2, end+1):
            tmp_max = max(cur, prev + nums[i])
            prev, cur = cur, tmp_max
        return cur
