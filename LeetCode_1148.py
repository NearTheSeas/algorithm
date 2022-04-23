""" 
https://leetcode-cn.com/problems/count-good-nodes-in-binary-tree/
1448. 统计二叉树中好节点的数目
"""
from base import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def traverse(node, curmx):
            if not node:
                return
            if node.val >= curmx:
                self.res += 1
            curmx = max(node.val, curmx)
            traverse(node.left, curmx)
            traverse(node.right, curmx)
        traverse(root, -float('inf'))
        return self.res
