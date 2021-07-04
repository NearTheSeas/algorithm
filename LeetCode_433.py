""" 
https://leetcode-cn.com/problems/minimum-genetic-mutation/
433. 最小基因变化

求最短路径：广度优先遍历
遍历start
依次替换为map中的字符
判断是否合法
继续替换 or 回退
"""
from typing import List
import collections


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0

        level = 0
        bankSet = set(bank)
        hashMap = ['A', 'C', 'G', 'T']
        visited = set([start])

        # 还可以 (element, level)的形式
        q = collections.deque([start])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == end:
                    return level
                for i in range(8):
                    old = cur
                    for ch in hashMap:
                        cur = cur[:i] + ch + cur[i+1:]
                        if cur not in visited and cur in bankSet:
                            visited.add(cur)
                            q.append(cur)
                    cur = old
            level += 1

        return -1
