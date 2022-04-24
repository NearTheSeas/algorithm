""" 
https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
剑指 Offer 32 - III. 从上到下打印二叉树 III

遍利用双端队列的两端皆可添加元素的特性，设打印列表（双端队列） tmp ，并规定：
奇数层 则添加至 tmp 尾部 ，
偶数层 则添加至 tmp 头部 。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from base import TreeNode
from typing import List
import collections


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        res = []
        while q:
            tmp = collections.deque()
            for _ in range(len(q)):
                node = q.popleft()
                if len(res) % 2:
                    tmp.appendleft(node.val)  # 偶数层 -> 队列头部
                else:
                    tmp.append(node.val)  # 奇数层 -> 队列尾部
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(list(tmp))
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        res = []
        mask = 1
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(tmp[::-1] if mask < 0 else tmp)
            mask *= -1
        return res
