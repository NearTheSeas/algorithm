""" 
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
二叉树的前序遍历
"""
from base import TreeNode
from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root: TreeNode, res: List[int]) -> None:
        if not root:
            return None
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)
