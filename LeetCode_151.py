""" 
https://leetcode-cn.com/problems/reverse-words-in-a-string/
151. 翻转字符串里的单词

字符串不可变 首先得把字符串转化成其他可变的数据结构，同时还需要在转化的过程中去除空格
字符串两端 trim
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
