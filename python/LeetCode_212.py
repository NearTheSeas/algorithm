""" 
https://leetcode-cn.com/problems/word-search-ii/
212. 单词搜索 II
trie + 回溯
"""
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = "$"
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node[WORD_KEY] = word
        rows, columns = len(board), len(board[0])
        result = []

        def backtrack(row, col, parent):
            ch = board[row][col]
            node = parent[ch]
            wordMatched = node.pop(WORD_KEY, False)
            if wordMatched:
                result.append(wordMatched)
            board[row][col] = '#'
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row+rowOffset, col+colOffset
                if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= columns:
                    continue
                if board[newRow][newCol] not in node:
                    continue
                backtrack(newRow, newCol, node)
            board[row][col] = ch

        for row in range(rows):
            for col in range(columns):
                if board[row][col] in trie:
                    backtrack(row, col, trie)
        return result
