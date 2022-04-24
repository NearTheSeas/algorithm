""" 
https://leetcode-cn.com/problems/opLdQZ/
剑指 Offer II 056. 二叉搜索树中两个节点之和
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        cache = []
        cur, stack = root, []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if (k - cur.val) in cache:
                return True
            cache.append(cur.val)
            cur = cur.right

        return False
