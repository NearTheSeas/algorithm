""" 
https://leetcode-cn.com/problems/A1NYOS/
剑指 Offer II 011. 0 和 1 个数相同的子数组
"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumMap = dict()
        sumMap[0] = -1
        preSum, ans = 0, 0
        for i in range(len(nums)):
            preSum += -1 if nums[i] == 0 else 1
            # 求的是最长，所以只记录第一个 preSum出现的位置
            # 当再次出现preSum这个前缀和，求子数组长度
            if preSum in sumMap:
                ans = max(ans, i - sumMap[preSum])
            else:
                sumMap[preSum] = i
        return ans
