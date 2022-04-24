""" 
https://leetcode-cn.com/problems/NYBBNL/
剑指 Offer II 052. 展平二叉搜索树
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        pre = dummy

        def dfs(root):
            nonlocal pre
            if not root:
                return

            dfs(root.left)
            pre.right = root
            pre.left = None
            pre = root
            dfs(root.right)

        dfs(root)
        return dummy.right

    def increasingBST2(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        prev, cur, stack = dummy, root, []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            prev.right = cur
            cur.left = None
            prev = cur
            cur = cur.right
        return dummy.right
