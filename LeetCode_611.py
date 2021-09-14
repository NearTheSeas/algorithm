""" 
https://leetcode-cn.com/problems/valid-triangle-number/
611. 有效三角形的个数

数组排序
有效三角形：nums[k]<nums[i]+nums[j] 
"""
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            k = i
            for j in range(i+1, n):
                while k+1 < n and nums[k+1] < nums[i]+nums[j]:
                    k += 1
                ans += max(k-j, 0)
        return ans
