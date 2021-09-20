""" 
https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
剑指 Offer 46. 把数字翻译成字符串
"""


class Solution:
    def translateNum(self, num: int) -> int:
        str_num = str(num)
        n = len(str_num)
        dp = [1]*(n+1)
        for i in range(2, n+1):
            if 10 <= int(str_num[i-2:i]) < 26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]
