""" 
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

删除有序数组中的重复项
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
from types import List


def removeDuplicates(nums: List[int]) -> int:
    n = len(nums)
    if not nums or n <= 0:
        return 0
    cur = 1
    for i in range(1, n):
        if nums[i] != nums[i-1]:
            nums[cur] = nums[i]
            cur += 1
    return cur
