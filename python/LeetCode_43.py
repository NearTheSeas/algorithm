""" 
https://leetcode-cn.com/problems/multiply-strings/
43. 字符串相乘
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        ans = '0'
        m, n = len(num1), len(num2)
        ansArr = [0]*(m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                ansArr[i+j+1] += int(num1[i])*int(num2[j])
        for i in range(m+n-1, 0, -1):
            ansArr[i-1] += ansArr[i] // 10
            ansArr[i] %= 10
        index = 1 if ansArr[0] == 0 else 0
        ans = ''.join(str(x) for x in ansArr[index:])
        return ans
