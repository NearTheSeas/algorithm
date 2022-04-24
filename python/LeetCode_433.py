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

    def minMutation2(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        if end not in bank:
            return -1
        level = 0
        bankSet = set(bank)
        if start in bankSet:
            bankSet.remove(start)
        hashMap = ['A', 'C', 'G', 'T']
        front = {start}
        back = {end}

        while front:
            level += 1
            next_front = set()
            for cur in front:
                for i in range(8):
                    for ch in hashMap:
                        newStr = cur[:i] + ch + cur[i+1:]
                        if newStr in back:
                            return level
                        if newStr in bankSet:
                            next_front.add(newStr)
                            bankSet.remove(newStr)
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return -1
