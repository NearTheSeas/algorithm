""" 
https://leetcode-cn.com/problems/om3reC/
剑指 Offer II 108. 单词演变
"""
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        front = set([beginWord])
        end = set([endWord])
        notVisited = set(wordList)
        n = len(beginWord)
        steps = 1
        while front:
            steps += 1
            neighbours = set()
            for word in front:
                for i in range(n):
                    for j in range(26):
                        ch = chr(ord('a')+j)
                        if ch != word[i]:
                            new_Word = word[:i] + ch + word[i+1:]
                            if new_Word in end:
                                return steps
                            if new_Word in notVisited:
                                neighbours.add(new_Word)
                                notVisited.remove(new_Word)
            front = neighbours
            if len(front) > len(end):
                front, end = end, front
        return 0
