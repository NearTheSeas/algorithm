""" 
https://leetcode-cn.com/problems/race-car/
818. 赛车

目标位置 i
连续k个A到达位置S(k)，1个掉头，后退S(k)-i步
k-1个A到达S(k-1)，掉头R，回退一定步数A，再前进R， 前进一定步数A
"""


class Solution:
    def racecar(self, target: int) -> int:
        dp = [0, 1, 4] + [float('inf')]*(target)
        for t in range(3, target+1):
            k = t.bit_length()
            # k个A 刚好到达t
            if t == 2**k-1:
                dp[t] = k
                continue
            # 倒退j步 2个R
            for j in range(k-1):
                # 前进k-1步，回退j步，再前进
                dp[t] = min(dp[t], dp[t-(2**(k-1)-2**j)] + k-1 + j + 2)
            if 2**k - 1 - t < t:
                # 前进k步 超过了t
                dp[t] = min(dp[t], dp[2**k-1-t]+k+1)

        return dp[target]
