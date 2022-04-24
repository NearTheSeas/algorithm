""" 
https://leetcode-cn.com/problems/P5rCT8/
剑指 Offer II 053. 二叉搜索树中的中序后继
"""

# Definition for a binary tree node.
from typing import Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        cur = root
        fount = False
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if fount:
                break
            elif cur == p:
                fount = True
            cur = cur.right
        return cur

    def inorderSuccessor2(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        cur = root
        res = None
        while cur:
            if cur.val > p.val:
                res = cur
                cur = cur.left
            else:
                cur = cur.right
        return res
