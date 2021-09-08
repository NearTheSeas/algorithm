"""
https://leetcode-cn.com/problems/super-egg-drop/
887. 鸡蛋掉落

k个鸡蛋 n层楼
"""


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = dict()

        def dp(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float('inf')
            for i in range(1, n+1):
                res = min(res, max(dp(k, n-i), dp(k-1, i-1))+1)
            memo[(k, n)] = res
            return res
        return dp(k, n)

    def superEggDrop2(self, k: int, n: int) -> int:
        memo = dict()

        def dp(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float('inf')
            lo, hi = 1, n
            while lo <= hi:
                mid = (lo+hi)//2
                broken = dp(k-1, mid-1)
                not_broken = dp(k, n-mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
            memo[(k, n)] = res
            return res
        return dp(k, n)
