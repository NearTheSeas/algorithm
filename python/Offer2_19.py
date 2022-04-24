""" 
https://leetcode-cn.com/problems/RQku0D/
剑指 Offer II 019. 最多删除一个字符得到回文
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)
        while l < r:
            if s[l] != s[r]:
                return self.check(s, l+1, r) or self.check(s, l, r-1)
            l += 1
            r -= 1
        return True

    def check(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
