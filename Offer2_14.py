"""
https://leetcode-cn.com/problems/MPnaiL/
剑指 Offer II 014. 字符串中的变位词
"""

import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts = [0]*26
        for i in range(len(s1)):
            counts[ord(s1[i]) - ord('a')] += 1
            counts[ord(s2[i]) - ord('a')] -= 1
        if self.allZero(counts):
            return True

        for i in range(len(s1), len(s2)):
            counts[ord(s2[i]) - ord('a')] -= 1
            counts[ord(s2[i - len(s1)]) - ord('a')] += 1
            if self.allZero(counts):
                return True
        return False

    def allZero(self, counts):
        for num in counts:
            if num != 0:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)

        for c in s1:
            need[c] += 1

        left = 0
        for right, ch in enumerate(s2):
            window[ch] += 1
            while window[ch] > need[ch]:
                d = s2[left]
                window[d] -= 1
                left += 1
            if right - left + 1 == len(s1):
                return True
        return False
