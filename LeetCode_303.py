""" 
https://leetcode-cn.com/problems/range-sum-query-immutable/
303. 区域和检索 - 数组不可变
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums
        for num in nums:
            _sums.append(_sums[-1]+num)

    def sumRange(self, left: int, right: int) -> int:
        _sums = self.sums
        return _sums[right+1] - _sums[left]
