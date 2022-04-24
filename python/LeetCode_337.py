""" 
https://leetcode-cn.com/problems/house-robber-iii/
337. 打家劫舍 III

不能同时选中父子节点
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root:
                return 0, 0

            left = _rob(root.left)
            right = _rob(root.right)

            # 偷当前节点， left[1] right[1] 表示子节点不偷的值
            v1 = root.val + left[1] + right[1]
            v2 = max(left) + max(right)  # 不偷当前节点 去左右子节点最大值
            return v1, v2
        return max(_rob(root))
