""" 
https://leetcode-cn.com/problems/count-complete-tree-nodes/
222. 完全二叉树的节点个数
"""

from base import TreeNode
import collections


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = 0
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            result += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
