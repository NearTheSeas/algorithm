""" 
https://leetcode-cn.com/problems/h54YBf/
剑指 Offer II 048. 序列化与反序列化二叉树
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from base import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + ',' + right

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper(dataList):
            val = dataList.pop(0)
            if val == '#':
                return None
            node = TreeNode(val)
            node.left = helper(dataList)
            node.right = helper(dataList)
            return node
        return helper(data.split(','))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
