""" 
https://leetcode-cn.com/problems/LwUNpT/
剑指 Offer II 045. 二叉树最底层最左边的值
"""

# Definition for a binary tree node.

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        que = collections.deque([root])
        bottomLeft = root.val
        while que:
            n = len(que)
            for i in range(n):
                node = que.popleft()
                if i == 0:
                    bottomLeft = node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return bottomLeft
