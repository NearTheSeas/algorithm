"""
https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/
剑指 Offer 37. 序列化二叉树
"""

# Definition for a binary tree node.


import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append('null')
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(str(x) for x in res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        def dfs(data):
            if not data:
                return
            val = data.pop(0)
            if val == 'null':
                return None
            node = TreeNode(val)
            node.left = dfs(data)
            node.right = dfs(data)
            return node
        return dfs(data.split(','))

    def serialize(self, root):
        if not root:
            return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]":
            return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
