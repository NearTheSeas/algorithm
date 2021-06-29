""" 
https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
N 叉树的后序遍历
"""
from base import Node
from typing import List

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        self.dfs(root, res)
        return res

    def dfs(self, root: 'Node', res: List[int]) -> None:
        if not root:
            return
        if root.children:
            for node in root.children:
                self.dfs(node, res)
        res.append(root.val)
        
  
    