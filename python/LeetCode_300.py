""" 
   https://leetcode-cn.com/problems/longest-increasing-subsequence/
   300. 最长递增子序列

   dp[i] 为考虑前i个元素，以第i个数字结尾的最长上升子序列的长度
   """

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        tails, res = [0]*len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                mid = (i+j)//2
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = num
            if j == res:
                res += 1
        return res
