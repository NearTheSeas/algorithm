""" 
https://leetcode-cn.com/problems/JFETK5/
剑指 Offer II 002. 二进制加法
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a)-1, len(b)-1
        result, carry = [], 0
        while m >= 0 or n >= 0 or carry:

            if m >= 0:
                n1 = int(a[m])
                m -= 1
            else:
                n1 = 0
                
            if n >= 0:
                n2 = int(b[n])
                n -= 1
            else:
                n2 = 0

            tmp = n1 + n2 + carry
            carry = 1 if tmp >= 2 else 0
            result.append(str(tmp % 2))
        return ''.join(result[::-1])
