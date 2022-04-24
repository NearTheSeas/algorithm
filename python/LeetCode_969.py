""" 
https://leetcode-cn.com/problems/pancake-sorting/
969. 煎饼排序
"""
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        res = []
        idx = arr.index(max(arr))
        # 将最大的翻到顶部
        arr = arr[:idx+1][::-1] + arr[idx+1:]
        #  整体翻转 最大的翻到底部
        arr = arr[::-1]
        res += [idx+1, len(arr)]
        tmp = self.pancakeSort(arr[:-1])
        res = res + tmp
        return res

    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        length = len(arr)
        while length > 0:
            idx = arr.index(max(arr[:length]))
            # 第一次翻转
            arr = arr[:idx+1][::-1] + arr[idx+1:]
            res.append(idx+1)
            # 第二次翻转
            arr = arr[:length][::-1]
            res.append(length)
            length -= 1
        return res
