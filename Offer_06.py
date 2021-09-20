""" 
https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
剑指 Offer 06. 从尾到头打印链表
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from base import ListNode
from typing import List


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []

        def traverse(node):
            nonlocal res
            if not node:
                return None
            traverse(node.next)
            res.append(node.val)
        traverse(head)
        return res
