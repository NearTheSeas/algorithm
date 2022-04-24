""" 
https://leetcode-cn.com/problems/UHnkqh/
剑指 Offer II 024. 反转链表
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from base import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre
