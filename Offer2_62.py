""" 
https://leetcode-cn.com/problems/QC3q1f/
剑指 Offer II 062. 实现前缀树
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None]*26
        self.isEnd = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                return False
            node = node.children[ch]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                return False
            node = node.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
