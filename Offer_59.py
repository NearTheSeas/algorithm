""" 
https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/
剑指 Offer 59 - I. 滑动窗口的最大值
"""


import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()

        for i in range(k):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
        res = [nums[window[0]]]
        for i in range(k, len(nums)):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
            while window[0] <= i-k:
                window.popleft()
            res.append(nums[window[0]])
        return res
