""" 
剑指 Offer 60. n个骰子的点数
"""

from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1/6]*6
        for i in range(2, n+1):
            # 点数之和的值最大是i*6，最小是i*1
            # 比如i=3个骰子时，最小就是3了，不可能是2和1
            # 所以点数之和的值的个数是6*i-(i-1)，化简：5*i+1
            tmp = [0]*(5*i+1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j+k] += dp[j]/6
            dp = tmp
        return dp
