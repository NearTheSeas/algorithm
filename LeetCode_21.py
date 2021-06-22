""" 
https://leetcode-cn.com/problems/merge-two-sorted-lists/
合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
from base import ListNode


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(-1)
    prev = head
    while l1 and l2:
        if l1.val > l2.val:
            prev.next = l2
            l2 = l2.next
        else:
            prev.next = l1
            l1 = l1.next
        prev = prev.next
    if not l1:
        prev.next = l2
    if not l2:
        prev.next = l1
    return head.next
