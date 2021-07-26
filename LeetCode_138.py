""" 
https://leetcode-cn.com/problems/copy-list-with-random-pointer/
138. 复制带随机指针的链表

迭代 + 节点拆分

在每个节点后，增加一个copy节点，
每个copy节点指向原节点的random节点
拆分链表
"""
from base import Node


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # 复制节点
        front = head
        while front:
            node = Node(front.val, None, None)
            node.next = front.next
            front.next = node
            front = node.next

        # 复制 random
        front = head
        while front:
            if front.random:
                front.next.random = front.random.next
            front = front.next.next
        # 拆分
        front = head
        dumy = Node(-1, None, None)
        cur = dumy
        while front:
            cur.next = front.next
            cur = cur.next
            front.next = cur.next
            front = front.next

        return dumy.next
