""" 
https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/
363. 矩形区域不超过 K 的最大数值和

前缀和 + 二分
Sr - Sl < k
Sl < Sr - k
"""
from typing import List

from sortedcontainers.sortedlist import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = -float('inf')
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]

                totalSet = SortedList([0])
                s = 0
                for v in total:
                    s += v
                    # bisect_left 二分插入
                    lb = totalSet.bisect_left(s-k)
                    if lb != len(totalSet):
                        ans = max(ans, s-totalSet[lb])
                    totalSet.add(s)
