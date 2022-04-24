""" 
https://leetcode-cn.com/problems/6eUYwP/
剑指 Offer II 050. 向下的路径节点之和
"""

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        preSum = collections.defaultdict(int)
        preSum[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            res = 0
            curr += root.val
            res += preSum[curr - targetSum]
            preSum[curr] += 1
            res += dfs(root.left, curr)
            res += dfs(root.right, curr)
            preSum[curr] -= 1
            return res
        return dfs(root, 0)
