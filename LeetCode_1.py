"""
https://leetcode-cn.com/problems/two-sum/
两数和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

1. 暴力双循环
2. hashtable key是数值 value是序号
3. 先排序 然后双指针
"""
from types import List


def twoSum(nums: List[int], target: int) -> List[int]:
    if not nums:
        return[]
    table = dict()
    for i, num in enumerate(nums):
        if target - num in table:
            return [table[target-num], i]
        table[num] = i
    return []
