""" 
https://leetcode-cn.com/problems/vlzXQL/
剑指 Offer II 111. 计算除法
"""
from typing import List
import collections


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(int)
        letters = set()
        for i, [a, b] in enumerate(equations):
            graph[(a, b)] = values[i]
            graph[(b, a)] = 1.0/values[i]
            letters.add(a)
            letters.add(b)

        letters = list(letters)
        for k in range(letters):
            for i in range(letters):
                for j in range(letters):
                    if graph[(i, k)] and graph[(k, j)]:
                        graph[(i, j)] = graph[(i, k)]*graph[(k, j)]
        res = []
        for x, y in queries:
            if graph[(x, y)]:
                res.append(graph[(x, y)])
            else:
                res.append(-1.0)
        return res
