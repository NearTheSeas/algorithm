"""
https://leetcode-cn.com/problems/reverse-linked-list-ii/
92. 反转链表 II
反转指定位置的链表
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dumyHead = ListNode(0)
        dumyHead.next = head

        pre, count = dumyHead,  1

        while pre.next and count < left:
            pre = pre.next
            count += 1
        cur = pre.next
        while cur and count < right:
            moved = cur.next
            cur.next = cur.next.next
            moved.next = pre.next
            pre.next = moved
            count += 1

        return dumyHead.next
