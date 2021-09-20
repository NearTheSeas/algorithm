""" 
https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
剑指 Offer 12. 矩阵中的路径

DFS 
标记当前矩阵元素： 将 board[i][j] 修改为 空字符 '' ，
代表此元素已访问过，防止之后搜索时重复访问。
搜索下一单元格： 朝当前元素的 上、下、左、右 四个方向开启下层递归，
使用 或 连接 （代表只需找到一条可行路径就直接返回，不再做后续 DFS ），并记录结果至 res 。
还原当前矩阵元素： 将 board[i][j] 元素还原至初始值，即 word[k]
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def trace(i, j, k):
            res = False
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False

            if k == len(word)-1:
                return True
            board[i][j] = ''
            for i_new, j_new in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if trace(i+i_new, j+j_new, k+1):
                    return True
            board[i][j] = word[k]
            return res

        for i in range(m):
            for j in range(n):
                if trace(i, j, 0):
                    return True
        return False
