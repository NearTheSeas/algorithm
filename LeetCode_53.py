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

    def maxSubArray2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        pre, ans = nums[0], 0
        for num in nums:
            pre = max(num, pre + num)
            ans = max(ans, pre)
        return ans
