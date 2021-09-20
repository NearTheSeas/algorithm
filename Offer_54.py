""" 
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
剑指 Offer 54. 二叉搜索树的第k大节点
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from base import TreeNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            dfs(node.left)
        self.k = k
        dfs(root)
        return self.res
