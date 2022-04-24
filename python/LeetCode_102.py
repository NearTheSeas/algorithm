""" 
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
102. 二叉树的层序遍历
"""
from base import TreeNode
from typing import List
import collections


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = collections.deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result
