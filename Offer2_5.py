""" 
https://leetcode-cn.com/problems/aseY1I/
剑指 Offer II 005. 单词长度的最大乘积
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask_map, ans = {}, 0
        for word in words:
            bitmask = 0
            for c in word:
                bitmask |= 1 << (ord(c) - ord('a')) # 1 左移  ord(c) - ord('a') 位
            if bitmask in bitmask_map:
                bitmask_map[bitmask] = max(bitmask_map[bitmask], len(word))
            else:
                bitmask_map[bitmask] = len(word)

        for x in bitmask_map:
            for y in bitmask_map:
                if (x & y) == 0:
                    ans = max(ans, bitmask_map[x]*bitmask_map[y])
        return ans
