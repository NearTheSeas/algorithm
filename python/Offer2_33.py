""" 
https://leetcode-cn.com/problems/sfvd7V/
剑指 Offer II 033. 变位词组
"""
from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for s in strs:
            k = ''.join(sorted(list(s)))
            hashmap[k].append(s)
        return list(hashmap.values())
