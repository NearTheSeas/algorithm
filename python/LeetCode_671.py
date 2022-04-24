""" 
https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/
671. 二叉树中第二小的节点

bfs dfs 找到第一个比跟节点小的节点
"""

from base import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ans, rootvalue = -1, root.val

        def dfs(node: TreeNode):
            nonlocal ans
            if not node:
                return
            if ans != -1 and node.val >= ans:
                return
            if node.val > rootvalue:
                ans = node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans
