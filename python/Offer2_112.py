""" 
https://leetcode-cn.com/problems/fpTFWP/
剑指 Offer II 112. 最长递增路径
"""
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        lengths = [[0]*n for _ in range(m)]
        res = 0

        def helper(i, j):
            # 查缓存
            if lengths[i][j] != 0:
                return lengths[i][j]
            # 默认是1 只会出现在周围元素都小于等于当前元素时
            length = 1
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                # 遍历周围元素 找更大的 递归直到最大的元素 length=1 然后逐步return 回来
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    length = max(length, helper(x, y)+1)
            lengths[i][j] = length
            return length

        for i in range(m):
            for j in range(n):
                res = max(res, helper(i, j))
        return res
