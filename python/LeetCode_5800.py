""" 
https://leetcode-cn.com/problems/build-array-from-permutation/
5800. 基于排列构建数组
"""

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            res.append(nums[n])
        return res
