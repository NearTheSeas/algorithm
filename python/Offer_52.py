""" 
https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
剑指 Offer 52. 两个链表的第一个公共节点
两个链表长度分别为L1+C、L2+C， C为公共部分的长度，
第一个人走了L1+C步后，回到第二个人起点走L2步；
第2个人走了L2+C步后，回到第一个人起点走L1步
当两个人走的步数都为L1+L2+C时相遇

最后一步有疑惑，感觉会陷入死循环，实际上不会，因为最后两人同时走到末尾，
都是 None，就结束循环了
"""

from base import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
