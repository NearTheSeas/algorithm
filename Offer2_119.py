""" 
https://leetcode-cn.com/problems/WhsWhI/
剑指 Offer II 119. 最长连续序列
"""

from typing import List
import collections


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        notVisited = set(nums)

        def helper(num):
            q = collections.deque([num])
            notVisited.remove(num)
            cnt = 1
            while q:
                num = q.popleft()
                for neighbour in [num-1, num+1]:
                    if neighbour in notVisited:
                        notVisited.remove(neighbour)
                        q.append(neighbour)
                        cnt += 1
            return cnt

        for num in nums:
            if num in notVisited:
                res = max(res, helper(num))
        return res
