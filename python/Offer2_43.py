""" 
https://leetcode-cn.com/problems/NaqhDT/
剑指 Offer II 043. 往完全二叉树添加节点
"""

import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.que = collections.deque([root])

        _que = self.que
        while _que[0].left and _que[0].right:
            node = _que.popleft()
            _que.append(node.left)
            _que.append(node.right)

    def insert(self, v: int) -> int:
        node = TreeNode(v)
        _que = self.que
        parent = _que[0]
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            _que.popleft()
            _que.append(parent.left)
            _que.append(parent.right)
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
