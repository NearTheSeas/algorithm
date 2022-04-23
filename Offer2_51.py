""" 
https://leetcode-cn.com/problems/jC7MId/
剑指 Offer II 051. 节点之和最大的路径
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            res = max(res, root.val + left + right)
            return root.val + max(left, right)
        dfs(root)
        return res
