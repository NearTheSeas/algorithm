""" 
https://leetcode-cn.com/problems/8Zf90G/
剑指 Offer II 036. 后缀表达式
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        calc = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: int(x/y),
        }
        for token in tokens:
            if token in tokens:
                num2, num1 = stack.pop(), stack.pop()
                stack.append(calc[token](num1, num2))
            else:
                stack.append(int(token))
        return stack[0]
