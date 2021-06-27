""" 
https://leetcode-cn.com/problems/sliding-window-maximum/
滑动窗口最大值
"""

from typing import Collection, List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = Collection.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ans = [nums[q[0]]]
        for i in range(k, len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i-k:
                q.popleft()
            ans.append(nums[q[0]])
        return ans
