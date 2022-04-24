""" 
https://leetcode-cn.com/problems/a7VOhD/
剑指 Offer II 020. 回文子字符串的个数
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        for i in range(len(s)):
            count += self.centerExpand(s, i, i)
            count += self.centerExpand(s, i, i+1)
        return count

    def centerExpand(s, start, end):
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            count += 1
        return count
