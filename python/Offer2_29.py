""" 
https://leetcode-cn.com/problems/4ueAj6/
剑指 Offer II 029. 排序的循环链表
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""




from base import Node
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            head = node
            head.next = head
        elif head.next == head:
            head.next = node
            node.next = head
        else:
            self.insertCore(head, node)
        return head

    def insertCore(self, head: 'Node', node: 'Node'):
        cur, nxt = head, head.next
        biggest = head
        while not (cur.val <= node.val and nxt.val >= node.val) and nxt != head:
            cur = nxt
            nxt = nxt.next
            if cur.val >= biggest.val:
                biggest = cur

        if cur.val <= node.val and nxt.val >= node.val:
            cur.next = node
            node.next = nxt
        else:
            node.next = biggest.next
            biggest.next = node
