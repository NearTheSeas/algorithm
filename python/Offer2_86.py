""" 
https://leetcode-cn.com/problems/M99OJA/
剑指 Offer II 086. 分割回文子字符串
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        dp = self.getPalindromes(s)
        self.helper(s, dp, 0, [], res)
        return res

    def helper(self, s, dp, idx, substrings, res):
        if idx == len(s):
            res.append(substrings[:])
            return

        for i in range(idx, len(s)):
            if dp[idx][i]:
                substrings.append(s[idx: i+1])
                self.helper(s, dp,  i+1, s, res)
                substrings.pop()

    def getPalindromes(self, s):
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1:
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
        return dp
