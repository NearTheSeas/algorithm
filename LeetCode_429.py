"""
https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
N 叉树的层序遍历

给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
"""

from base import Node
from typing import List
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                q.extend(node.children)
            res.append(level)
        return res
