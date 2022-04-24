""" 
https://leetcode-cn.com/problems/7WqeDu/
剑指 Offer II 057. 值和下标之差都在给定的范围内
"""
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        w = t+1

        def get_bucket_id(num):
            if num >= 0:
                return num // w
            else:
                return int((num+1)/w) - 1
        bucket = dict()
        for i, num in enumerate(nums):
            ID = get_bucket_id(num)
            if ID in bucket:
                return True
            if ID - 1 in bucket and num - bucket[ID - 1] <= t:
                return True
            if ID + 1 in bucket and bucket[ID + 1] - num <= t:
                return True
            bucket[ID] = num
            if i >= k:
                del_ID = get_bucket_id(nums[i-k])
                del bucket[del_ID]
        return False
