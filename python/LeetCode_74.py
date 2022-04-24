""" 
https://leetcode-cn.com/problems/search-a-2d-matrix/
74. 搜索二维矩阵
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = 0, len(matrix[0])-1
        while m <= len(matrix)-1 and n >= 0:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                n -= 1
            else:
                m += 1
        return False
