""" 
https://leetcode-cn.com/problems/validate-binary-search-tree/
98. 验证二叉搜索树

1) 中序遍历是升序的
2) 辅助函数 根节点是每棵左子树的最大值，是每棵右字数的最小值
"""
from base import TreeNode


class Solution:
    # 中序遍历
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], float('-inf')
        while stack or root:
            # 一直找到最小值
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True

    def isValidBST2(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True
            val = node.val

            if val <= lower or val >= upper:
                return False
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False

        return helper(root)
