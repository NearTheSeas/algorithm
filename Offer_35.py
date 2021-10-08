""" 
https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
剑指 Offer 35. 复杂链表的复制
"""

# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur = head
        while cur:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node
            cur = node.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = res = head.next
        pre = head
        while cur.next:
            # 顺序不能乱
            pre.next = pre.next.next
            cur.next = cur.next.next
            cur = cur.next
            pre = pre.next
        pre.next = None # 需要单独处理
        return res
