""" 
https://leetcode-cn.com/problems/longest-palindromic-substring/
5. 最长回文子串
中心扩散
枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止
中心点可以是一个字符 也可以是两个字符
"""


class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right+1
        return left+1, right-1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)
            if right1 - left1 > end - start:
                start, end = left1, right1

            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end+1]
