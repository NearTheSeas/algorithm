""" 
https://leetcode-cn.com/problems/vvXgSW/
剑指 Offer II 078. 合并排序链表
"""
from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.mergeList(lists, 0, len(lists)-1)

    def mergeList(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = start + (end - start) // 2
        head1 = self.mergeList(lists, start, mid)
        head2 = self.mergeList(lists, mid+1, end)
        return self.merge(head1, head2)

    def merge(self, head1, head2):
        dummy = ListNode()
        cur = dummy
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 if head1 else head2
        return dummy.next
