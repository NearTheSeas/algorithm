""" 
https://leetcode-cn.com/problems/Jf1JuT/
剑指 Offer II 114. 外星文字典
"""
from typing import List
import collections


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = collections.defaultdict(list)
        indegrees = dict()
        for word in words:
            for ch in word:
                if ch not in indegrees:
                    indegrees[ch] = 0

        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            # 特殊用例  ["abc","ab"]
            if w1.startswith(w2) and w1 != w2:
                return ''
            minLength = min(len(w1), len(w2))
            for j in range(minLength):
                ch1 = w1[j]
                ch2 = w2[j]
                if ch1 != ch2:
                    if ch2 not in graph[ch1]:
                        graph[ch1].append(ch2)
                        indegrees[ch2] += 1
                    break
        q = collections.deque()
        for ch, count in indegrees.items():
            if count == 0:
                q.append(ch)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nxt in graph[node]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    q.append(nxt)
        return ''.join(res) if len(res) == len(indegrees) else ""
