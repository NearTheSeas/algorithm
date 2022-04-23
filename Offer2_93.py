""" 
https://leetcode-cn.com/problems/Q91FMA/
剑指 Offer II 093. 最长斐波那契数列
"""
from typing import List
import collections


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hashmap = {num: i for i, num in enumerate(arr)}
        dic = collections.defaultdict(lambda: 2)
        res = 2
        for end, num in enumerate(arr):
            for mid in range(end):
                start = hashmap.get(num - arr[mid], None)
                if start is not None and start < mid:
                    dic[mid, end] = dic[start, mid]+1
                    res = max(res, dic[mid, end])
        return res if res > 2 else 0
