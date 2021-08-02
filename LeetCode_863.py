""" 
https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/
863. 二叉树中所有距离为 K 的结点

构建图 或者 hashmap 记录节点的父节点
"""
from base import TreeNode
import collections
from typing import List


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node_parent = dict()

        def dfs_find_parent(node: TreeNode) -> None:
            if node:
                if node.left:
                    node_parent[node.left] = node
                if node.right:
                    node_parent[node.right] = node
                dfs_find_parent(node.left)
                dfs_find_parent(node.right)

        dfs_find_parent(root)
        if k == 0:
            return [target.val]

        ans = []
        q = collections.deque()
        visited = set()
        q.append(target)
        visited.add(target)
        level = 0
        while q and level < k:
            level += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for nei in [node_parent[cur] if cur in node_parent else None, cur.left, cur.right]:
                    if nei and nei not in visited:
                        if level == k:
                            ans.append(nei.val)
                        q.append(nei)
                        visited.add(nei)
        return ans

    def distanceK2(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node_parent = dict()

        def dfs_find_parent(node: TreeNode) -> None:
            if node:
                if node.left:
                    node_parent[node.left] = node
                if node.right:
                    node_parent[node.right] = node
                dfs_find_parent(node.left)
                dfs_find_parent(node.right)
        dfs_find_parent(root)

        def dfs_find_ans(node: TreeNode, prev: TreeNode, cur_dis: int) -> None:
            if node:
                if cur_dis == k:
                    ans.append(node.val)
                if node.left != prev:
                    dfs_find_ans(node.left, node, cur_dis + 1)
                if node.right != prev:
                    dfs_find_ans(node.right, node, cur_dis+1)
                if node in node_parent and node_parent[node] != prev:
                    dfs_find_ans(node_parent[node], node, cur_dis+1)

        ans = []
        dfs_find_ans(target, None, 0)
        return ans
