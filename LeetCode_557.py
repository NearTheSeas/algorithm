""" 
https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
557. 反转字符串中的单词 III
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split())
