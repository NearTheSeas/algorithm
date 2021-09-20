""" 
https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
剑指 Offer 42. 连续子数组的最大和
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, pre = float('-inf'), float('-inf')
        for num in nums:
            pre = max(num, num+pre)
            ans = max(ans, pre)
        return ans
