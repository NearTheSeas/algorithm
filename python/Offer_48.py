""" 
https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
剑指 Offer 48. 最长不含重复字符的子字符串
"""

import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        dic = {}
        dp = [1]*n
        for j, ch in enumerate(s):
            i = dic.get(ch, -1)
            dic[ch] = j
            if dp[j-1] < j-i:
                dp[j] = dp[j-1]+1
            else:
                dp[j] = j - i
        return max(dp)

    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j, ch in enumerate(s):
            i = dic.get(ch, -1)
            dic[ch] = j
            tmp = tmp + 1 if tmp < j-i else j-i
            res = max(res, tmp)
        return res

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
