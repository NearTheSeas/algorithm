""" 
https://leetcode-cn.com/problems/kTOapQ/
剑指 Offer II 055. 二叉搜索树迭代器
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.cur = root
        self.stack = []

    def next(self) -> int:
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        val = self.cur.val
        self.cur = self.cur.right
        return val

    def hasNext(self) -> bool:
        return bool(self.cur or self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
