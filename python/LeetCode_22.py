""" 
https://leetcode-cn.com/problems/generate-parentheses/
22. 括号生成

左右括号各n个
每次递归 
    左括号数量小于n
    右括号数量小于左括号
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generate(0, 0, n, "", res)
        return res

    def generate(self, left: int, right: int, n: int, s: str, res: List) -> str:
        if left == n and right == n:
            res.append(s)
            return

        if left < n:
            self.generate(left+1, right, n, s+'(', res)

        if right < left:
            self.generate(left, right+1, n, s+')', res)
