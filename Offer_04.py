""" 
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
剑指 Offer 04. 二维数组中的查找
"""

from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:

            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True

        return False
