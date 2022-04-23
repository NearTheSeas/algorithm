""" 
https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
剑指 Offer 22. 链表中倒数第k个节点

需要考虑k超过链表长度
"""

from base import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
