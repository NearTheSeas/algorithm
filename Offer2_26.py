""" 
https://leetcode-cn.com/problems/LGjMqU/
剑指 Offer II 026. 重排链表
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from base import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode()
        dummy.next = head
        fast, slow = dummy, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        slow.next = None
        tmp = self.reverseList(tmp)
        self.linkList(head, tmp, dummy)

    def linkList(self, l1, l2, head):
        prev = head
        while l1 and l2:
            tmp = l1.next

            prev.next = l1
            l1.next = l2
            prev = l2

            l1 = tmp
            l2 = l2.next
        if l1:
            prev.next = l1

    def reverseList(self, l):
        prev = None
        while l:
            tmp = l.next
            l.next = prev
            prev = l
            l = tmp
        return prev

    # 利用list
    def reorderList2(self, head: ListNode) -> None:
        if not head:
            return

        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1

        vec[i].next = None
