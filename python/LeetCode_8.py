""" 
https://leetcode-cn.com/problems/string-to-integer-atoi/
8. 字符串转换整数 (atoi)

确定有限状态机 状态转移矩阵
正负判别
超长溢出
"""


INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self) -> None:
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans += self.ans*10 + int(c)
            self.ans = min(self.ans, INT_MAX)if self.sign == 1 else min(
                self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == "+" else -1


class Solution:
    def myAtoi(self, s: str) -> int:
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        return automaton.sign * automaton.ans
