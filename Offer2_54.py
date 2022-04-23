""" 
https://leetcode-cn.com/problems/w6cpku/
剑指 Offer II 054. 所有大于等于节点的值之和
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        cur, stack, preSum = root, [], 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            preSum += cur.val
            cur.val = preSum
            cur = cur.left
        return root
