""" 
https://leetcode-cn.com/problems/VabMRr/
剑指 Offer II 015. 字符串中的所有变位词
"""

from typing import List
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n, res = len(s), len(p), []
        if m < n:
            return []

        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in p:
            need[c] += 1

        left = 0
        for right, ch in enumerate(s):
            window[ch] += 1
            while window[ch] > need[ch]:
                d = s[left]
                window[d] -= 1
                left += 1
            if right - left + 1 == n:
                res.append(left)

        return res
