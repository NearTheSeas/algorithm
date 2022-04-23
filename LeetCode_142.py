""" 
https://leetcode-cn.com/problems/linked-list-cycle-ii/
142. 环形链表 II

返回环的起点
"""

from base import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
