""" 
https://leetcode-cn.com/problems/surrounded-regions/
130. 被围绕的区域

从边界的o开始深度优先遍历，相邻的o标记为特殊字符
任何边界上的 O 都不会被填充为 X。 我们可以想到，
所有的不被包围的 O 都直接或间接与边界上的 O 相连。我们可以利用这个性质判断 O 是否在边界上，具体地说：

对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O；
最后我们遍历这个矩阵，对于每一个字母：
如果该字母被标记过，则该字母为没有被字母 X 包围的字母 O，我们将其还原为字母 O；
如果该字母没有被标记过，则该字母为被字母 X 包围的字母 O，我们将其修改为字母 X。

"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != 'O':
                return

            board[x][y] = 'A'
            for row, col in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                dfs(row, col)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for i in range(n-1):
            dfs(0, i)
            dfs(m-1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
