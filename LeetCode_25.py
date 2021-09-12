"""
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
25. K 个一组翻转链表
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode, tail: ListNode):
        pre, cur = tail.next, head
        while pre != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nxt = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nxt
            pre = tail
            head = tail.next
        return hair.next
