""" 
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
剑指 Offer 33. 二叉搜索树的后序遍历序列

划分左右子树： 
    遍历后序遍历的[i,j] 区间元素，
    寻找第一个大于根节点的节点，索引记为 m
    可划分出左子树区间 [i,m-1]右子树区间 [m,j−1]
    根节点索引 j
"""

from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and recur(i, m-1) and recur(m, j-1)

        return recur(0, len(postorder)-1)

    # ???
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack, root = [], float('inf')
        for i in range(len(postorder)-1, -1, -1):
            if postorder[i] > root:
                return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
            return True
