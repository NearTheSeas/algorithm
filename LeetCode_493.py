"""
https://leetcode-cn.com/problems/reverse-pairs/
493. 翻转对

分治 合的过程中计算逆序对
"""
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0

        def mergeSort(nums: List[int], left: int, right: int):
            if left < right:
                mid = left + (right-left) // 2
                mergeSort(nums, left, mid)
                mergeSort(nums, mid+1, right)
                merge(nums, left, right)

        def merge(nums: List[int], left: int, right: int) -> None:
            mid = left + (right-left) // 2
            i, j = left, mid+1
            tmp = []
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            ii, jj = left, mid+1
            while ii <= mid and jj <= right:
                if nums[ii] <= 2 * nums[jj]:
                    ii += 1
                else:
                    self.cnt += (mid-ii+1)
                    jj += 1
            if i <= mid:
                tmp += nums[i:mid+1]
            if j <= right:
                tmp += nums[j:right+1]
            for i in range(len(tmp)):
                nums[left+i] = tmp[i]

        mergeSort(nums, 0, len(nums)-1)
        return self.cnt