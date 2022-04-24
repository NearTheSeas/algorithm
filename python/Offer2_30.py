""" 
https://leetcode-cn.com/problems/FortPu/
剑指 Offer II 030. 插入、删除和随机访问都是 O(1) 的容器
"""
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_idx = dict()
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.num_idx:
            return False
        self.num_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.num_idx:
            return False
        idx = self.num_idx[val]
        last_num = self.nums[-1]
        self.nums[idx] = last_num
        self.num_idx[last_num] = idx
        self.nums.pop()
        del self.num_idx[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.nums)-1)
        return self.nums[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
