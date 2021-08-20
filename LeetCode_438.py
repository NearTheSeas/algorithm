""" 
https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
438. 找到字符串中所有字母异位词

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
滑动窗口
"""

from typing import List
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n, ans = len(s), len(p), []
        if m < n:
            return ans
        need = collections.defaultdict(int)
        hasCnt = collections.defaultdict(int)
        for c in p:
            need[c] += 1
        left = 0
        for right, c in enumerate(s):
            hasCnt[c] += 1
            while hasCnt[c] > need[c]:
                d = s[left]
                hasCnt[d] -= 1
                left += 1
            if right - left + 1 == n:
                ans.append(left)
        return ans
