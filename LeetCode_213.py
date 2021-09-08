""" 
https://leetcode-cn.com/problems/house-robber-ii/
213. 打家劫舍 II
房屋连成圈 间隔取值
如果偷窃了第一间房屋，则不能偷窃最后一间房屋，因此偷窃房屋的范围是第一间房屋到最后第二间房屋；则偷窃房屋的下标范围是 [0, n-2]
如果偷窃了最后一间房屋，则不能偷窃第一间房屋，因此偷窃房屋的范围是第二间房屋到最后一间房屋。偷窃房屋的下标范围是 [1, n-1]

范围取值


"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(start: int, end: int) -> int:
            first, second = nums[start], max(nums[start], nums[start+1])
            for i in range(start, end):
                first, second = second, max(first+nums[i], second)

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            return max(robRange(0, n-2), robRange(1, n-1))
