""" 
https://leetcode-cn.com/problems/M1oyTv/
剑指 Offer II 017. 含有所有字符的最短字符串
"""

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        count = len(need)
        start, end, valid = 0, len(s)+1, 0
        left = 0
        for right, ch in enumerate(s):
            window[ch] += 1
            if need[ch] and window[ch] == need[ch]:
                valid += 1
            while valid == count:
                if right - left < end - start:
                    start, end = left, right
                d = s[left]
                left += 1
                if need[d] and window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
        return "" if end - start == len(s)+1 else s[start:end+1]
