""" 
https://leetcode-cn.com/problems/word-ladder/
127. 单词接龙
"""
import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordSet = set(wordList)
        layer = {}
        # key 是目标词   value 是到达目标词的转换路径
        layer[beginWord] = [[beginWord]]

        while layer:
            newLayer = collections.defaultdict(list)
            for word in layer:  # 遍历 key 也就是上一轮生成的新词
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            # 新词都是在当前词的路径上变化而来
                            newLayer[newWord] += [j + [newWord]
                                                  for j in layer[word]]
            wordSet -= set(newLayer.keys()) # 避免重复访问
            layer = newLayer
        return []
