""" 
https://leetcode-cn.com/problems/ms70jA/
剑指 Offer II 067. 最大的异或
"""

from typing import List


class Trie:
    def __init__(self):
        self.child = [None for _ in range(2)]

    def insert(self, x: int) -> None:
        root = self
        for i in range(30, -1, -1):
            ID = (x >> i) & 1
            if root.child[ID] == None:
                root.child[ID] = Trie()
            root = root.child[ID]

    def query(self, x: int) -> int:
        root = self
        res = 0
        for i in range(30, -1, -1):
            ID = (x >> i) & 1
            if root.child[1 - ID] != None:
                res = res * 2 + 1
                root = root.child[1 - ID]
            else:
                res = res * 2
                root = root.child[ID]
        return res


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)

        T = Trie()
        res = 0
        for x in nums:
            T.insert(x)
            res = max(res, T.query(x))
        return res
