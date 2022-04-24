""" 
https://leetcode-cn.com/problems/frog-jump/
403. 青蛙过河

dp[i][k] 表示青蛙能否达到「现在所处的石子编号」为 i 且「上一次跳跃距离」为 k 的状态。

kstones[i]−stones[j]=k
dp[i][k] = dp[j][k-1] | dp[j][k] | dp[j][k+1]

dp[0][0]=true
"""

import collections
from functools import lru_cache
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @lru_cache
        def dfs(pos, step):
            if pos == stones[-1]:
                return True
            for d in [-1, 0, 1]:
                if step+d > 0 and pos+step+d in set(stones):
                    if dfs(pos+step+d, step+d):
                        return True
            return False
        pos, step = 0, 0
        return dfs(pos, step)

    def canCross2(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False]*n for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):  # 依次遍历全部石头
            for j in range(i-1, -1, -1):  # 遍历当前石头之前历史
                k = stones[i] - stones[j]
                if k > j+1:
                    break
                dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
        return any(dp[-1])
