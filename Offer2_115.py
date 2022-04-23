""" 
https://leetcode-cn.com/problems/ur2n8P/
剑指 Offer II 115. 重建序列
"""

from typing import List
import collections


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = dict()
        for seq in seqs:
            for num in seq:
                if num not in indegrees:
                    indegrees[num] = 0
            for i in range(len(seq)-1):
                num1 = seq[i]
                num2 = seq[i+1]
                if num2 not in graph[num1]:
                    graph[num1].append(num2)
                    indegrees[num2] += 1
        if len(org) != len(indegrees):
            return False
        q = collections.deque()
        for num, cnt in indegrees.items():
            if cnt == 0:
                q.append(num)

        res = []
        while len(q) == 1:
            num = q.popleft()
            res.append(num)
            for nxt in graph[num]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    q.append(nxt)

        return org == res
