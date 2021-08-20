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
                    if need[d] == 0:  # 碰到了恰好数量合适的字符
                        break
                    need[d] += 1
                    left += 1
                if right-left < end-start:
                    start, end = left, right
                need[s[left]] += 1  # 寻找新的满足条件滑动窗口
                needCnt += 1
                left += 1
        return '' if end > len(s) else s[start:end+1]

    def minWindow2(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        cache = len(need)
        left, right = 0, 0
        valid, minLength = 0, float('inf')
        start, end = 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            if need[c]:
                window[c] += 1
                if need[c] == window[c]:
                    valid += 1

            while valid == cache:
                if right - left < minLength:
                    start, end = left, right
                    minLength = right - left
                d = s[left]
                left += 1
                if need[d]:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if minLength == float('inf') else s[start:end+1]
