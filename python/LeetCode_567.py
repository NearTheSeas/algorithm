""" 
https://leetcode-cn.com/problems/permutation-in-string/
567. 字符串的排列
"""

import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if n < m:
            return False

        need = collections.defaultdict(int)
        window = collections.defaultdict(int)

        for c in s1:
            need[c] += 1

        left = 0
        for right, c in enumerate(s2):
            window[c] += 1
            while window[c] > need[c]:
                d = s2[left]
                window[d] -= 1
                left += 1
            if right - left + 1 == m:
                return True

        return False
