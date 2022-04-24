""" 
https://leetcode-cn.com/problems/n-queens/
51. N 皇后
方向一的斜线为从左上到右下方向，同一条斜线上的每个位置满足行下标与列下标之差相等，例如 (0,0)(0,0) 和 (3,3)(3,3) 在同一条方向一的斜线上。因此使用行下标与列下标之差即可明确表示每一条方向一的斜线
方向二的斜线为从右上到左下方向，同一条斜线上的每个位置满足行下标与列下标之和相等，例如 (3,0)(3,0) 和 (1,2)(1,2) 在同一条方向二的斜线上。因此使用行下标与列下标之和即可明确表示每一条方向二的斜线。

首先迭代row
再一次尝试col
判断当前 row,col 组合是否可行
回溯
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def generateBoard():
            board = list()
            for i in range(n):
                row = ['.'] * n
                row[queens[i]] = "Q"
                board.append(''.join(row))
            return board

        def backtrack(row: int) -> None:
            if row == n:
                board = generateBoard()
                result.append(board)
            else:
                for col in range(n):
                    if col in columns or row - col in diagonal1 or row + col in diagonal2:
                        continue
                    queens[row] = col
                    columns.add(col)
                    diagonal1.add(row-col)
                    diagonal2.add(row+col)
                    backtrack(row+1)
                    columns.remove(col)
                    diagonal1.remove(row-col)
                    diagonal2.remove(row+col)

        result = []
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        backtrack(0)
        return result
    
    
    def solveNQueens2(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
