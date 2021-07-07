""" 
https://leetcode-cn.com/problems/palindromic-substrings/
647. 回文子串

回文判断：中心拓展
中心点不能只有单个字符构成，还要包括两个字符，
比如上面这个子串 abab，就可以有中心点 ba 扩展一次得到，
所以最终的中心点由 2 * len - 1 个，分别是 len 个单字符和 len - 1 个双字符

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for center in range(len(s)*2-1):
            left = center >> 1
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
