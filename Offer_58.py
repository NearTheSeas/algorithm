""" 
https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
剑指 Offer 58 - I. 翻转单词顺序
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])
