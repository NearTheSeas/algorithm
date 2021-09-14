""" 
https://leetcode-cn.com/problems/binary-search/
704. 二分查找
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid-1
            else:
                lo = mid + 1
        return -1
