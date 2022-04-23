""" 
https://leetcode-cn.com/problems/iSwD2y/
剑指 Offer II 065. 最短的单词编码
"""
from typing import List


class Trie:
    def __init__(self):
        self.children = [None]*26

    def insert(self, word):
        node = self
        for ch in word[::-1]:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = self.buildTrie(words)
        res = 0

        def dfs(root, i):
            nonlocal res
            isLeaf = True
            for child in root.children:
                if child:
                    isLeaf = False
                    dfs(child, i+1)
            if isLeaf:
                res += i
        dfs(root, 1)
        return res

    def buildTrie(self, words):
        root = Trie()
        for word in words:
            root.insert(word)
        return root
