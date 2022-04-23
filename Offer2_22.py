""" 
https://leetcode-cn.com/problems/c32eOV/
剑指 Offer II 022. 链表中环的入口节点
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from base import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
