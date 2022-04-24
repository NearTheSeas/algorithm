"""
https://leetcode-cn.com/problems/7LpjUW/
剑指 Offer II 118. 多余的边
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            parent[find(i)] = parent[find(j)]

        for x, y in edges:
            if find(x) != find(y):
                union(x, y)
            else:
                return [x, y]
        return []