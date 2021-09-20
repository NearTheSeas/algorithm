""" 
https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
剑指 Offer 24. 反转链表
"""
from base import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur,pre = head,None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
