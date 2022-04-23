""" 
https://leetcode-cn.com/problems/O4NDxx/
剑指 Offer II 013. 二维子矩阵的和
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sums = [[0]*(n+1) for _ in range(m+1)]
        _sums = self.sums
        for i in range(m):
            rowSum = 0
            for j in range(n):
                rowSum += matrix[i][j]
                _sums[i+1][j+1] = _sums[i][j+1] + rowSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums
        return _sums[row2+1][col2+1] - _sums[row2+1][col1] - _sums[row1][col2 + 1] + _sums[row1][col1]

    # Your NumMatrix object will be instantiated and called as such:
    # obj = NumMatrix(matrix)
    # param_1 = obj.sumRegion(row1,col1,row2,col2)
