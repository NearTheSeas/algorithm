""" 
https://leetcode-cn.com/problems/vEAB3K/
剑指 Offer II 106. 二分图
"""
from typing import List
import collections


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLOR, GREEN, RED = 0, 1, 2
        colors = [UNCOLOR]*(n)
        for i in range(n):
            if colors[i] == UNCOLOR:
                q = collections.deque([i])
                colors[i] = GREEN
                while q:
                    node = q.popleft()
                    colorNei = RED if colors[node] == GREEN else GREEN
                    for neighbour in graph[node]:
                        if colors[neighbour] == UNCOLOR:
                            q.append(neighbour)
                            colors[neighbour] = colorNei
                        elif colors[neighbour] != colorNei:
                            return False
        return True
