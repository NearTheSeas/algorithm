""" 
https://leetcode-cn.com/problems/maximum-product-subarray/
152. 乘积最大子数组

考虑当前位置如果是一个负数的话，那么我们希望以它前一个位置结尾的某个段的积也是个负数，这样就可以负负得正，并且我们希望这个积尽可能「负得更多」，即尽可能小。
如果当前位置是一个正数的话，我们更希望以它前一个位置结尾的某个段的积也是个正数，并且希望它尽可能地大。

"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result, imax, imin = -float('inf'), 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax*nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])

            result = max(result, imax)
        return result
