""" 
https://leetcode-cn.com/problems/7WHec2/
剑指 Offer II 077. 链表排序
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head1 = head
        head2 = self.split(head)
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.merge(head1, head2)

    def split(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        return second

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
