""" 
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/
188. 买卖股票的最佳时机 IV
我们用 buy[i][j] 表示对于数组prices[0..i] 中的价格而言，进行恰好 j 笔交易，并且当前手上持有一支股票，这种情况下的最大利润；
用 sell[i][j] 表示恰好进行 j 笔交易，并且当前手上不持有股票，这种情况下的最大利润。

buy[i][j]=max{buy[i−1][j],sell[i−1][j]−price[i]}
sell[i][j]=max{sell[i−1][j],buy[i−1][j−1]+price[i]}

通用模型：
用 n 表示股票价格数组的长度；
用 i 表示第 i 天（i 的取值范围是 0 到 n - 1）；
用 k 表示允许的最大交易次数；
用 T[i][k] 表示在第 i 天结束时，最多进行 k 次交易的情况下可以获得的最大收益

T[i][k][0] 表示在第 i 天结束时，最多进行 k 次交易且在进行操作后持有 0 份股票的情况下可以获得的最大收益；
T[i][k][1] 表示在第 i 天结束时，最多进行 k 次交易且在进行操作后持有 1 份股票的情况下可以获得的最大收益。

T[-1][k][0] = 0, 
T[-1][k][1] = -Infinity
T[i][0][0] = 0, 
T[i][0][1] = -Infinity

T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k - 1][0] - prices[i])

"""
from typing import List


class Solution:
    

    def maxProfit(self, k: int, prices: List[int]) -> int:
        k = min(k, len(prices) // 2)

        buy = [-float("inf")] * (k+1)
        sell = [0] * (k+1)

        for p in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1] - p)
                sell[i] = max(sell[i], buy[i] + p)

        return sell[-1]
    
    def maxProfit2(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]

        buy[0][0], sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float("-inf")

        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])

        return max(sell[n - 1])


