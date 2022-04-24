""" 
https://leetcode-cn.com/problems/WNC0Lk/
剑指 Offer II 046. 二叉树的右侧视图
"""
from typing import List
import collections
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        que = collections.deque([root])
        res = []
        while que:
            n = len(que)
            for i in range(n):
                node = que.popleft()
                if i == n-1:
                    res.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res
