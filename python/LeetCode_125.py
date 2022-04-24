""" 
https://leetcode-cn.com/problems/valid-palindrome/
125. 验证回文串

原字符串上判断
判断左右值是否是字符或者数字 
判断left<right
判断大小写
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n-1
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1

        return True

    def isPalindrome2(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1

        return True
