""" 
https://leetcode-cn.com/problems/H6lPxb/
剑指 Offer II 117. 相似的字符串
"""

from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        fathers = list(range(n))
        groups = n

        def union(i, j):
            p1 = find(i)
            p2 = find(j)
            if p1 != p2:
                fathers[p1] = p2
                return True
            return False

        def find(i):
            if fathers[i] != i:
                fathers[i] = find(fathers[i])
            return fathers[i]

        for i in range(n):
            for j in range(i+1, n):
                if self.similar(strs[i], strs[j]) and union(i, j):
                    groups -= 1
        return groups

    def similar(self, str1, str2):
        cnt = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                cnt += 1
        return cnt <= 2
