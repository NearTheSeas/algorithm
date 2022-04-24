""" 
https://leetcode-cn.com/problems/QTMn0o/
剑指 Offer II 010. 和为 k 的子数组
"""

from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumToCount = collections.defaultdict(int)
        sumToCount[0] = 1
        preSum, count = 0, 0
        for num in nums:
            preSum += num
            count += sumToCount[preSum - k]
            sumToCount[preSum] += 1
        return count
