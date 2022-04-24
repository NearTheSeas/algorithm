""" 
https://leetcode-cn.com/problems/lMSNwu/
剑指 Offer II 025. 链表中的两数相加
"""
from base import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        dummy = ListNode()
        cur = dummy
        plus = 0
        while l1 or l2 or plus:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            tmp = n1 + n2 + plus
            plus = 1 if tmp >= 10 else 0
            node = ListNode(tmp % 10)
            cur.next = node
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return self.reverseList(dummy)

    def reverseList(self, l):
        prev = None
        while l:
            tmp = l.next
            l.next = prev
            prev = l
            l = tmp
        return prev
