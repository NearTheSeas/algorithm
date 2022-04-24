""" 
https://leetcode-cn.com/problems/subarray-sum-equals-k/
560. 和为K的子数组

前缀和 + hashmap
"""
from typing import Counter, List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_times = collections.defaultdict(int)
        num_times[0] = 1
        cur_sum = 0
        res = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in num_times:
                res += num_times[Counter-k]
            num_times[cur_sum] += 1
        return res
