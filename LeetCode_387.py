""" 
https://leetcode-cn.com/problems/first-unique-character-in-a-string/
387. 字符串中的第一个唯一字符
"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1
