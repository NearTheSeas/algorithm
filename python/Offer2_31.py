""" 
https://leetcode-cn.com/problems/OrIXps/
剑指 Offer II 031. 最近最少使用缓存
"""


class ListNode:
    def __init__(self, key=0, value=0, ) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.hashmap = dict()

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            node = ListNode(key, value)
            self.hashmap[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.hashmap.pop(removed.key)
                self.size -= 1
        else:
            node = self.hashmap[key]
            node.value = value
            self.moveToHead(node)

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
