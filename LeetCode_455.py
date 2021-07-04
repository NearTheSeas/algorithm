""" 
https://leetcode-cn.com/problems/assign-cookies/
455. 分发饼干
"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m, n = len(g), len(s)
        i = j = counter = 0
        while i < m and j < n:
            while j < n and g[i] > s[j]:
                j += 1
            if j < n:
                counter += 1
            i += 1
            j += 1
        return counter
