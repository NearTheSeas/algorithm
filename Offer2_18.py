""" 
https://leetcode-cn.com/problems/XltzEq/
剑指 Offer II 018. 有效的回文
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum() and right > left:
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
