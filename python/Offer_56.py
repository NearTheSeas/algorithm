""" 
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
剑指 Offer 56 - I. 数组中数字出现的次数

利异或 将两个未重复的数字分到两个不同的组
"""

from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        x, y, n, m = 0, 0, 0, 1
        for num in nums:
            n ^= num
        while n & m == 0:
            m <<= 1
        for num in nums:
            if num & m:
                x ^= num
            else:
                y ^= num
        return x, y
