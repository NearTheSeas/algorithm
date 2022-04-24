"""
https://leetcode-cn.com/problems/word-ladder-ii/
126. 单词接龙 II
"""

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        visited = set()
        visited.add(beginWord)
        visited.add(endWord)

        begin_visited = set()
        begin_visited.add(beginWord)

        end_visited = set()
        end_visited.add(endWord)

        word_len = len(beginWord)
        step = 1

        while begin_visited and end_visited:
            if len(begin_visited) > len(end_visited):
                begin_visited, end_visited = end_visited, begin_visited

            next_round = set()
            for word in begin_visited:
                word_list = list(word)
                for i in range(word_len):
                    old_char = word_list[i]
                    for j in range(26):
                        word_list[i] = chr(ord('a') + j)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word in end_visited:
                                return step + 1
                            if next_word not in visited:
                                next_round.add(next_word)
                                visited.add(next_word)
                    word_list[i] = old_char
            begin_visited = next_round
            step += 1
        return 0
