""" 
https://leetcode-cn.com/problems/invert-binary-tree/
226. 翻转二叉树
"""
from base import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
