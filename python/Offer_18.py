""" 
https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
剑指 Offer 18. 删除链表的节点
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from base import ListNode


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        dummy = ListNode(0)
        dummy.next = head
        while head.next.val != val:
            head = head.next
        head.next = head.next.next
        return dummy.next
