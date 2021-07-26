""" 
https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/
1713. 得到子序列的最少操作次数


求出最长公共子序列的长度n，len(target) - n 为结果，复杂度 O(n * m)

当其中一个数组元素各不相同时，最长公共子序列问题（LCS）可以转换为最长上升子序列问题（LIS）进行求解。
同时最长上升子序列问题（LIS）存在使用「维护单调序列 + 二分」的贪心解法，复杂度为 O(nlogn)

1143. 最长公共子序列
300. 最长递增子序列
"""
from typing import List
import bisect


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        idx_dict = {num: i for i, num in enumerate(target)}
        stack = []
        for num in arr:
            if num in idx_dict:
                idx = idx_dict[num]
                i = bisect.bisect_left(stack, idx)
                if i == len(stack):
                    stack.append(0)
                stack[i] = idx
        return len(target) - len(stack)
