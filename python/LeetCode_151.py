""" 
https://leetcode-cn.com/problems/reverse-words-in-a-string/
151. 翻转字符串里的单词

字符串不可变 首先得把字符串转化成其他可变的数据结构，同时还需要在转化的过程中去除空格
字符串两端 trim
"""
import collections


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right += 1

        q, word = collections.deque(), []
        while left <= right:
            if s[left] == ' ' and word:
                q.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1

        q.appendleft(''.join(word))

        return ' '.join(q)
