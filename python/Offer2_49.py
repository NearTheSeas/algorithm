""" 
https://leetcode-cn.com/problems/3Etpl5/
剑指 Offer II 049. 从根节点到叶节点的路径数字之和
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, path):
            if not root:
                return 0
            path = path * 10 + root.val
            if not root.left or not root.right:
                return path
            return dfs(root.left, path) + dfs(root.right, path)

        return dfs(root, 0)
