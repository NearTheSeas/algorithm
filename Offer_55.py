""" 
https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
剑指 Offer 55 - I. 二叉树的深度
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from base import TreeNode

import collections


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque([root])
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth
