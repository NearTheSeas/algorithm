""" 
https://leetcode-cn.com/problems/reverse-only-letters/
917. 仅仅反转字母
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)
