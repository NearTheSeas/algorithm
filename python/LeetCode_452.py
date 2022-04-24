""" 
https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/
452. 用最少数量的箭引爆气球

考虑所有气球中右边界位置最靠左的那一个，那么一定有一支箭的射出位置就是它的右边界（否则就没有箭可以将其引爆了）
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: x[1])
        right = points[0][1]
        merged = 1
        for i in range(1, n):
            if points[i][0] > right:
                merged += 1
                right = points[i][1]

        return merged
