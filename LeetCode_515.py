""" 
https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
515. 在每个树行中找最大值
"""

from typing import List
from base import TreeNode
import collections


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        q = collections.deque([root])
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(max(level))
        return result
