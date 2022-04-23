""" 
https://leetcode-cn.com/problems/spiral-matrix/
54. 螺旋矩阵
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        res = []
        while True:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break

            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break

            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res
