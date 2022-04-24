"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
3. 无重复字符的最长子串
"""

import collections


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)
        left, ans = 0, 0
        for right, c in enumerate(s):
            window[c] += 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            ans = max(right - left + 1, ans)
        return ans
