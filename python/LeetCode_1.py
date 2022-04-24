"""
https://leetcode-cn.com/problems/two-sum/
1. 两数之和

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
