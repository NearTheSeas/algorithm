""" 
https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/
剑指 Offer 55 - II. 平衡二叉树
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from base import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(node):
            if not node:
                return 0
            left = recur(node.left)
            if left == -1:
                return -1

            right = recur(node.right)
            if right == -1:
                return -1

            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return recur(root) != -1
