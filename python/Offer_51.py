""" 
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
剑指 Offer 51. 数组中的逆序对
"""

from typing import List


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(l, r):
            if l >= r:
                return 0
            mid = l+(r-l) // 2
            res = mergeSort(l, mid) + mergeSort(mid+1, r)
            i, j = l, mid+1
            tmp[l:r+1] = nums[l:r+1]
            for k in range(l, r+1):
                if i == mid+1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += mid-i+1
            return res

        n = len(nums)
        tmp = [0]*n
        return mergeSort(0, n-1)
