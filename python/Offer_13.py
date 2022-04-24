""" 
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
剑指 Offer 13. 机器人的运动范围
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def sums(x):
            s = 0
            while x != 0:
                s += x % 10
                x = x // 10
            return s

        def trace(i, j):
            if i >= m or j >= n or k < sums(i) + sums(j) or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + trace(i + 1, j) + trace(i, j + 1)
        visited = set()
        return trace(0, 0)
