""" 
https://leetcode-cn.com/problems/two-sum-iii-data-structure-design/
170. 两数之和 III 数据结构设计
"""


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums_count = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.nums_count:
            self.nums_count[number] += 1
        else:
            self.nums_count[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.nums_count.keys():
            other = value - num
            if num != other:
                if other in self.nums_count:
                    return True
            elif self.nums_count[num] > 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
