""" 
https://leetcode-cn.com/problems/longest-common-subpath/
5803. 最长公共子路径
"""

from typing import List


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        base, mod = 97755331, 49999 ** 4 * 3 * 7
        m = len(paths)

        def check(length: int) -> bool:
            if length == 0:
                return True

            bucket = set()

            for i in range(m):
                hash_i = 0
                for j in range(length):
                    hash_i = (hash_i * base + paths[i][j]) % mod
                bucket_i = {hash_i}

                mult = pow(base, length - 1, mod)
                for j in range(length, len(paths[i])):
                    hash_i = (
                        (hash_i - paths[i][j - length] * mult) * base + paths[i][j]) % mod
                    bucket_i.add(hash_i)

                if i == 0:
                    bucket = bucket | bucket_i
                else:
                    bucket = bucket & bucket_i

            if bucket:
                return True

            else:
                return False

        k = min([len(x) for x in paths])
        left, right = 0, k
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
