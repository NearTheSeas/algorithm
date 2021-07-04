""" 
https://leetcode-cn.com/problems/maximum-subarray/
53. 最大子序和
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = nums[0]
        for i in range(1, len(nums)):
            pre = max(pre + nums[i], nums[i])
            ans = max(pre, ans)
        return ans
