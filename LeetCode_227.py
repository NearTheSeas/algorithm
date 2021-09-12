"""
https://leetcode-cn.com/problems/basic-calculator-ii/
227. 基本计算器 II
"""


class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        sign = '+'
        num = 0
        for i in range(n):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            if i == n-1 or c in '+-*/':
                if sign == "+":
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        return sum(stack)
