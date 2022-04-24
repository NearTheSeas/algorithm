""" 
https://leetcode-cn.com/problems/bLyHh0/
剑指 Offer II 116. 省份数量
"""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        res = 0

        def helper(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] and j not in visited:
                    visited.add(j)
                    helper(j)

        for i in range(len(isConnected)):
            if i not in visited:
                res += 1
                helper(i)
        return res

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:

        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(x: int, y: int) -> None:
            parent[find(x)] = find(y)

        provinces = len(isConnected)
        parent = list(range(provinces))
        for i in range(provinces):
            for j in range(i+1, provinces):
                if isConnected[i][j] == 1:
                    union(i, j)
        circles = sum(parent[i] == i for i in range(provinces))
        return circles
