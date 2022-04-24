""" 
https://leetcode-cn.com/problems/powx-n/
50. Pow(x, n)
特殊情况处理：
n < 0
n = 0
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(N:int)-> float:
            if N == 0 :
                return 1
            y = fastPow(N //2)
            return y * y if N % 2 == 0 else y * y * x
        return fastPow(n) if n > 0 else  1 / fastPow(-n)
