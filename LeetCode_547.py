"""
https://leetcode-cn.com/problems/number-of-provinces/
547. 省份数量
"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
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

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add[j]
                    dfs(j)

        provinces = len(isConnected)
        visited = set()
        ans = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                visited.add(i)

        return ans
