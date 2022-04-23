""" 
https://leetcode-cn.com/problems/Qv1Da2/
剑指 Offer II 028. 展平多级双向链表
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.flattenCore(head)
        return head

    def flattenCore(self, head: 'Node') -> 'Node':
        node = head
        while node:
            nxt, tail = node.next, tail
            if node.child:
                child = node.child
                childTail = self.flattenCore(node.child)
                node.child = None
                node.next = child
                child.prev = node
                childTail.next = nxt
                if nxt:
                    nxt.prev = childTail
                tail = childTail
            else:
                tail = node
            node = node.next
        return tail
