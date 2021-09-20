""" 
https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
剑指 Offer 45. 把数组排成最小的数
先移动j 后移动i
"""

from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(l, r):
            if l >= r:
                return
            i, j = l, r
            while i < j:
                while i < j and strs[j] + strs[l] >= strs[l] + strs[j]:
                    j -= 1
                while i < j and strs[i] + strs[l] <= strs[l] + strs[i]:
                    i += 1

                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l, i-1)
            quick_sort(i+1, r)

        strs = [str(num) for num in nums]
        quick_sort(0, len(strs)-1)
        return ''.join(strs)
