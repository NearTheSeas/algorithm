"""
https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
剑指 Offer 34. 二叉树中和为某一值的路径
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
from base import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res, path = [], []

        def recur(root, target):
            if not root:
                return
            target -= root.val
            path.append(root.val)
            if target == 0 and not root.left and not root.right:
                res.append(path[:])
            recur(root.left, target)
            recur(root.right, target)
            path.pop()
        recur(root, target)
        return res
