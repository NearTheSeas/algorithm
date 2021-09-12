""" 
https://leetcode-cn.com/problems/palindrome-linked-list/
234. 回文链表

1) 利用数组反转
2) 后序遍历
3) O(1)的空间，不考虑链表复原，快慢指针在寻找中间节点的过程中直接反转链表前半部分，
找到中间节点之后直接从中间向两边开始比较
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        return li == li[::-1]

    def isPalindrome2(self, head: ListNode) -> bool:
        left = head

        def traverse(right):
            nonlocal left
            if not right:
                return True
            res = traverse(right.next)
            res = res and (right.val == left.val)
            left = left.next
            return res

        return traverse(head)

    def isPalindrome3(self, head: ListNode) -> bool:
        pre, slow, fast = None, head, head
        while fast and fast.next:
            tmp = slow.next
            if pre:
                slow.next = pre
            pre = slow
            fast = fast.next.next
            slow = tmp
        if fast:
            slow = slow.next
        while slow:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        return True
