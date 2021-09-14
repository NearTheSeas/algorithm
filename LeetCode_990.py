""" 
https://leetcode-cn.com/problems/satisfiability-of-equality-equations/
990. 等式方程的可满足性
"""
from typing import List


class Solution:
    class UnionFound:
        def __init__(self) -> None:
            self.parent = list(range(26))

        def find(self, p):
            if self.parent[p] == p:
                return p
            self.parent[p] = self.find(self.parent[p])
            return self.parent[p]

        def union(self, p, q):
            self.parent[self.find(p)] = self.find(q)

    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UnionFound()
        for st in equations:
            if st[1] == '=':
                p = ord(st[0]) - ord("a")
                q = ord(st[3]) - ord("a")
                uf.union(p, q)

        for st in equations:
            if st[1] == '!':
                p = ord(st[0]) - ord("a")
                q = ord(st[3]) - ord("a")
                if uf.find(p) == uf.find(q):
                    return False
        return True
