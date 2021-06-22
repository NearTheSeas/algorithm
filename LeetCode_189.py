"""
https://leetcode-cn.com/problems/rotate-array/

旋转数组

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""
from types import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    start, end = 0, n-1
    reverse(nums, start, end)
    reverse(nums, start, k-1)
    reverse(nums, k, end)


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
