""" 
https://leetcode-cn.com/problems/basic-calculator/
224. 基本计算器
"""


class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10*num + int(c)
            elif c == '+' or c == '-':
                res += sign*num
                num = 0
                sign = 1 if c == '+' else '-'
            elif c == "(":
                # 之前的结果入栈 符号入栈 括号内部优先计算
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop()  # 符号
                res += stack.pop()  # 数值
        res += sign * num
        return res
