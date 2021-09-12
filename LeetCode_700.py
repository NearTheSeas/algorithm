""" 
https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
700. 二叉搜索树中的搜索
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
