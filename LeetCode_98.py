""" 
https://leetcode-cn.com/problems/validate-binary-search-tree/
98. 验证二叉搜索树
"""
from base import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
