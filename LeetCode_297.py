"""
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/ 
297. 二叉树的序列化与反序列化

遍历方式可以选择 前序遍历、后续遍历、广度优先遍历，方便找出根节点
"""


import collections
from base import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: strl
        """
        if not root:
            return 'null'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + str(left) + ',' + str(right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(dataList):
            val = dataList.pop(0)
            if val == 'null':
                return None
            root = TreeNode(int(val))
            root.left = dfs(dataList)
            root.right = dfs(dataList)
            return root
        dataList = data.split(',')
        return dfs(dataList)

    def serialize2(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return root
        res = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append('null')
            else:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
        return ",".join(str(x) for x in res)

    def deserialize2(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return data
        dataList = data.split(',')
        root = TreeNode(dataList[0])
        q = collections.deque([root])
        i = 1
        while q:
            node = q.popleft()
            left = dataList[i]
            i += 1
            if left != 'null':
                node.left = TreeNode(left)
                q.append(node.left)
            else:
                node.left = None
            right = dataList[i]
            i += 1
            if right != 'null':
                node.right = TreeNode(right)
                q.append(node.right)
            else:
                node.right = None
        return root
