""" 
https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
剑指 Offer 07. 重建二叉树
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from base import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def _buildTree(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None
            rootVal = preorder[preLeft]
            node = TreeNode(rootVal)
            rootInorder = keyMap[rootVal]
            leftLength = rootInorder - inLeft

            node.left = _buildTree(
                preLeft+1, preLeft+leftLength, inLeft, rootInorder-1)
            node.right = _buildTree(
                preLeft+leftLength+1, preRight, rootInorder+1, inRight)

            return node
        keyMap = {elm: i for i, elm in enumerate(inorder)}
        n = len(preorder)
        root = _buildTree(0, n-1, 0, n-1)
        return root
