""" 
https://leetcode-cn.com/problems/eliminate-maximum-number-of-monsters/
5801. 消灭怪物的最大数量
求每个怪物可以跑多少轮
排序
"""
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n, counter = len(dist), 0
        rounds = [dist[i]/speed[i] for i in range(n)]
        rounds.sort()
        for i in range(n):
            if rounds[i] > i:
                counter += 1
            else:
                return counter
        return counter
