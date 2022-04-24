""" 
https://leetcode-cn.com/problems/bP4bmD/
剑指 Offer II 110. 所有路径
"""

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def helper(idx, path):
            if idx == len(graph)-1:
                res.append(path[:])
                return
            for i in graph[idx]:
                path.append(i)
                helper(i, path)
                path.pop()

        helper(0, [0])
        return res
