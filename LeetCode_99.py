""" 
https://leetcode-cn.com/problems/recover-binary-search-tree/
99. 恢复二叉搜索树
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from base import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
        dfs(root)

        x, y = None, None
        pre = nodes[0]
        for i in range(1, len(nodes)):
            if nodes[i].val < pre.val:
                y = nodes[i]
                if not x:
                    x = pre
            pre = nodes[i]
        if x and y:
            x.val, y.val = y.val, x.val
