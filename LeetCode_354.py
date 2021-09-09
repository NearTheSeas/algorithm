""" 
https://leetcode-cn.com/problems/russian-doll-envelopes/
354. 俄罗斯套娃信封问题

数组 sort 传递key 定义排序规则

按照第一位升序，在第一维相同时第二维降序排序
在第二维中找递增子序列
"""

from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        f = [1]*n
        for i in range(n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    f[i] = max(f[i], f[j]+1)

        return max(f)
