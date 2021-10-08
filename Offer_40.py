"""
https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
剑指 Offer 40. 最小的k个数
"""

from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr):
            return arr

        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i:
                return quick_sort(l, i - 1)
            if k > i:
                return quick_sort(i + 1, r)
            return arr[:k]

        return quick_sort(0, len(arr) - 1)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quick_sort(arr, l, r):
            if l >= r:
                return
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            quick_sort(arr, l, i-1)
            quick_sort(arr, i+1, r)
        quick_sort(arr, 0, len(arr)-1)
        return arr[:k]
