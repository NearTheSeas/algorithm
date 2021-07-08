"""
https://leetcode-cn.com/problems/sudoku-solver/
37. 解数独
"""


def isValidSudoku(self, board: List[List[str]]) -> bool:
    row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
    col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
    block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

    # empty = []  # 收集需填数位置
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
            # else:
            #     empty.append((i, j))
    return True
