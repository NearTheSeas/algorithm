""" 
https://leetcode-cn.com/problems/magnetic-force-between-two-balls/
1552. 两球之间的磁力
"""

from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 判断间隔为 x 的情况下，是否能塞下 m 个球
        def check(x: int) -> bool:
            pre = position[0]
            cnt = 1
            for i in range(1, len(position)):
                if position[i] - pre >= x:
                    pre = position[i]
                    cnt += 1
            return cnt >= m

        position.sort()
        lo, hi, ans = 1, position[-1]-position[0], -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
