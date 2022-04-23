""" 
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
124. 二叉树中的最大路径和

可以是任意路径：先上升N个节点，又下降N个节点
某一节点的最大路径是包含左右节点的
但是在向上返回的时候，只能携带左或右节点
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from base import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = float('-inf')

        def _maxGain(node):
            nonlocal maxSum
            if not node:
                return 0
            left = max(_maxGain(node.left), 0)
            right = max(_maxGain(node.right), 0)

            priceNewPath = node.val + left + right
            maxSum = max(maxSum, priceNewPath)

            return node.val + max(left, right)
        _maxGain(root)
        return maxSum
