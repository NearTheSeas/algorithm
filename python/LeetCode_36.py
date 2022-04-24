"""
https://leetcode-cn.com/problems/valid-sudoku/
36. 有效的数独

块的序号 block = (row // 3)*3 + column//3 
"""
from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    b = (i // 3)*3 + j // 3
                    val = int(board[i][j])
                    if val not in row[i] & col[j] & block[b]:
                        return False
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3)*3 + j // 3].remove(val)

        return True
