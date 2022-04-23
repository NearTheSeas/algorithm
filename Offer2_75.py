""" 
https://leetcode-cn.com/problems/0H97ZC/
剑指 Offer II 075. 数组相对排序
"""
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        upper = max(arr1)
        frequency = [0] * (upper + 1)
        for x in arr1:
            frequency[x] += 1
        ans = list()
        for x in arr2:
            ans.extend([x]*frequency[x])
            frequency[x] = 0
        for x in range(upper+1):
            if frequency[x] > 0:
                ans.extend([x]*frequency[x])
        return ans
