""" 
https://leetcode-cn.com/problems/race-car/
818. 赛车

目标位置 i
连续k个A到达位置S(k)，1个掉头，后退S(k)-i步
k-1个A到达S(k-1)，掉头R，回退一定步数A，再前进R， 前进一定步数A
"""


class Solution:
    def racecar(self, target: int) -> int:
        dp = [1, 4] + [0]*(target)
        k, S = 2, 3  # S是位置，k是连续加速次数，S记录连续k个A指令达到的位置
        for i in range(3, target):
            if i == S:
                dp[i] = k
                k += 1
                S = (1 << k) - 1  # 2^k - 1
            else:
                #  情况1：连续k个A后，回退
                dp[i] = k+1+dp[S-i]
                # 情况2：连续k-1个A后，回退(0/1/.../k-2)步后，再前进
                for back in range(k-1):
                    # 回退后还需前进的距离：i+S(back)-S(k-1)
                    d = i + (1 << back) - (1 << (k-1))
                    dp[i] = min(dp[i], (k-1)+2+back+dp[d])

        return dp[target]
