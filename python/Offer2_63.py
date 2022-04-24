""" 
https://leetcode-cn.com/problems/UhWRSj/
剑指 Offer II 063. 替换单词
"""
from typing import List


class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isWord = False

    def insert(self, word: str) -> None:
        root = self
        for c in word:
            idx = ord(c) - ord('a')
            if root.children[idx] == None:
                root.children[idx] = Trie()
            root = root.children[idx]
        root.isWord = True

    def query(self, word: str) -> str:
        root = self
        i = 0
        for c in word:
            idx = ord(c) - ord('a')
            if root.children[idx] == None:  # 如果没有前缀，直接返回word
                return word
            root = root.children[idx]
            i += 1
            if root.isWord == True:
                break
        return word[: i]


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        T = Trie()
        for word in dictionary:
            T.insert(word)

        words = sentence.split(" ")
        for i, word in enumerate(words):
            words[i] = T.query(word)
        return ' '.join(words)
