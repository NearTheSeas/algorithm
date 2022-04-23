""" 
https://leetcode-cn.com/problems/SLwz0R/
剑指 Offer II 021. 删除链表的倒数第 n 个结点
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from base import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        # slow = dummy 为了找到目标节点的前置
        fast, slow = head, dummy
        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
