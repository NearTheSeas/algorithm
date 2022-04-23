""" 
https://leetcode-cn.com/problems/IDBivT/
剑指 Offer II 085. 生成匹配的括号
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, 0, 0, '', res)
        return res

    def helper(self, n, left, right, s, res):
        if left == n and right == n:
            res.append(s)
            return

        if left < n:
            self.helper(n, left+1, right, s+'(', res)

        if left > right:
            self.helper(n, left, right+1, s+')', res)
