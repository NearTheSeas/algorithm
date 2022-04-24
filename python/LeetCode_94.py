""" 
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
二叉树中序遍历
"""

from base import TreeNode
from typing import List


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root: TreeNode, res: List[int]) -> None:
        if not root:
            return None
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
