""" 
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
153. 寻找旋转排序数组中的最小值

考虑数组中的最后一个元素 xx：在最小值右侧的元素（不包括最后一个元素本身），它们的值一定都严格小于 xx；而在最小值左侧的元素，它们的值一定都严格大于 xx。因此，我们可以根据这一条性质，通过二分查找的方法找出最小值

"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]
