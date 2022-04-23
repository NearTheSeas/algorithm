""" 
https://leetcode-cn.com/problems/aMhZSa/
剑指 Offer II 027. 回文链表

当后半部分到达末尾则比较完成，可以忽略计数情况中的中间节点。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from base import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        dummy = ListNode()
        dummy.next = head
        fast, slow = dummy, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        secondHalf = slow.next
        secondHalf = self.reverseList(secondHalf)

        flag = True
        while flag and secondHalf:
            if head.val != secondHalf.val:
                flag = False
            head = head.next
            secondHalf = secondHalf.next
        return flag

    def reverseList(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

    # 使用了额外空间
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
