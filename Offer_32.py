""" 
https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
剑指 Offer 32 - I. 从上到下打印二叉树
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from base import TreeNode
from typing import List
import collections


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
