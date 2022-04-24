""" 
https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array/
1877. 数组中最大数对和的最小值

"""

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = -float('inf')
        for i in range(n >> 1):
            ans = max(ans, nums[i]+nums[n-1-i])
        return ans
