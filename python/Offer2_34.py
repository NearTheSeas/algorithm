""" 
https://leetcode-cn.com/problems/lwyVBB/
剑指 Offer II 034. 外星语言是否排序
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            l1, l2 = len(w1), len(w2)
            for j in range(max(l1, l2)):
                i1 = -1 if j >= l1 else hashmap[w1[j]]
                i2 = -1 if j >= l2 else hashmap[w2[j]]

                if i1 > i2:
                    return False

                if i1 < i2:
                    break
        return True
