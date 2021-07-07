""" 
https://leetcode-cn.com/problems/minimum-window-substring/
76. 最小覆盖子串
"""
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        left = 0
        # start, length = 0, float('inf')
        start, end = 0, float('inf')
        for right, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True:
                    d = s[left]
                    if need[d] == 0: # 碰到了恰好数量合适的字符
                        break
                    need[d] += 1
                    left += 1
                if right-left < end-start:
                    start, end = left, right
                need[s[left]] += 1 # 寻找新的满足条件滑动窗口
                needCnt += 1
                left += 1
        return '' if end > len(s) else s[start:end+1]
