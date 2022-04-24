""" 
https://leetcode-cn.com/problems/add-two-numbers/submissions/
2. 两数相加

微软 预面试 考察的不是逆序的，借助堆栈解决
"""

from base import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        plus = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2 or plus:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            tmp = n1 + n2 + plus
            plus = 1 if tmp >= 10 else 0
            cur.next = ListNode(tmp % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
