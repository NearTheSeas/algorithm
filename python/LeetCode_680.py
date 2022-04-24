"""
https://leetcode-cn.com/problems/valid-palindrome-ii/
680. 验证回文字符串 Ⅱ
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(x): return x == x[::-1]
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] == s[right]:
                left, right = left+1, right-1
            else:
                return isPalindrome(s[left+1: right+1]) or isPalindrome(s[left: right])
        return True
