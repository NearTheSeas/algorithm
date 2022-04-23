""" 
https://leetcode-cn.com/problems/dKk3P7/
剑指 Offer II 032. 有效的变位词
"""

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = collections.defaultdict(int)
        for c in s:
            hashmap[c] += 1

        for c in t:
            if hashmap[c] == 0:
                return False
            hashmap[c] -= 1
        return True
