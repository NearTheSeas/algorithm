""" 
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
105. 从前序与中序遍历序列构造二叉树

官方题解视频不错
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def _buildTree(preLeft: int, preRight: int, inLeft: int, inRight: int):
            if preLeft > preRight:
                return None

            # 前序遍历中的第一个节点就是根节点
            rootVal = preorder[preLeft]
            # 在中序遍历中定位根节点
            rootInorder = index[rootVal]

            # 先把根节点建立出来
            root = TreeNode(rootVal)
            # 得到左子树中的节点数目
            size_left_subtree = rootInorder - inLeft
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = _buildTree(
                preLeft + 1, preLeft + size_left_subtree, inLeft, rootInorder - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = _buildTree(
                preLeft + size_left_subtree + 1, preRight, rootInorder + 1, inRight)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return _buildTree(0, n - 1, 0, n - 1)
