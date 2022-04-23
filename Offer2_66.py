""" 
https://leetcode-cn.com/problems/z1R5dt/
剑指 Offer II 066. 单词之和
"""


class Trie:
    def __init__(self):
        self.children = [None]*26
        self.val = 0

    def insert(self, word, val):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.val = val


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = Trie()

    def insert(self, key: str, val: int) -> None:
        self.t.insert(key, val)

    def sum(self, prefix: str) -> int:
        node = self.t
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                return 0
            node = node.children[ch]
        return self.getSum(node)

    def getSum(self, node):
        if not node:
            return 0
        res = node.val
        for child in node.children:
            res += self.getSum(child)
        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
