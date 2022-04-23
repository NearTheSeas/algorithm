""" 
https://leetcode-cn.com/problems/569nqc/
剑指 Offer II 035. 最小时间差
"""

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 24*60:
            return 0

        mins = sorted(int(timePoint[:2])*60 + int(timePoint[3:])
                      for timePoint in timePoints)
        mins.append(mins[0] + 60*24)
        res = mins[-1]
        for i in range(1, len(mins)):
            res = min(res, mins[i] - mins[i-1])
        return res
