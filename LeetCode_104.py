"""
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
104. 二叉树的最大深度
"""

from base import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
