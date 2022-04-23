""" 
https://leetcode-cn.com/problems/hPov7L/
剑指 Offer II 044. 二叉树每层的最大值
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
    def largestValues(self, root: TreeNode) -> List[int]:
        que = collections.deque([root])
        res = []
        while que:
            n = len(que)
            maxVal = -float('inf')
            for _ in range(n):
                node = que.popleft()
                maxVal = max(maxVal, node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(maxVal)
        return res
