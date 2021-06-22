"""
https://leetcode-cn.com/problems/merge-sorted-array/
合并两个有序数组

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

1.先插入 后排序
2.前序 依次复制到新数组
2.倒叙直接使用原数组
"""
from types import List


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    end = m+n-1
    m = m-1
    n = n-1
    while m >= 0 or n >= 0:
        if m == -1:
            nums1[end] = nums2[n]
            n -= 1
        elif n == -1:
            nums1[end] = nums1[m]
            m -= 1
        elif nums1[m] > nums2[n]:
            nums1[end] = nums1[m]
            m -= 1
        else:
            nums1[end] = nums2[n]
            n -= 1
