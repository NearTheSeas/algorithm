""" 
https://leetcode-cn.com/problems/wtcaE1/
剑指 Offer II 016. 不含重复字符的最长子字符串
"""
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        window, ans = collections.defaultdict(int), 0
        left = 0
        for right, ch in enumerate(s):
            window[ch] += 1
            while window[ch] > 1:
                d = s[left]
                window[d] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
