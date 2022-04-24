""" 
https://leetcode-cn.com/problems/US1pGT/
剑指 Offer II 064. 神奇的字典
"""
import collections
from typing import List

# 统计模式
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mode_words = collections.defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in set(dictionary):
            for i in range(len(word)):
                mode = word[:i] + '*' + word[i+1:]
                self.mode_words[mode].add(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            mode = searchWord[:i] + '*' + searchWord[i+1:]
            if len(self.mode_words[mode]) > 1:
                return True
            if len(self.mode_words[mode]) == 1 and searchWord not in self.mode_words[mode]:
                return True
        return False


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

    def search(self, word: str) -> bool:
        root = self
        for c in word:
            ID = ord(c) - ord('a')
            if root.child[ID] == None:
                return False
            root = root.child[ID]
        return root.isWord == True


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        cur = self.trie
        for i in dictionary:
            cur.insert(i)

    def search(self, searchWord: str) -> bool:
        sn = len(searchWord)
        # 每次替换 searchWord 的一个字符
        # 查找替换了一个字符的词 是否在字典树中
        for i in range(sn):
            for ID in range(26):
                nc = chr(ord('a') + ID)
                if searchWord[i] != nc:
                    next_word = searchWord[:i] + nc + searchWord[i+1:]
                    if self.trie.search(next_word) == True:
                        return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
