""" 
https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
剑指 Offer 38. 字符串的排列

注意去重
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        res, c = [], list(s)

        def recur(x):
            if x == len(c)-1:
                res.append(''.join(c[:]))
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                recur(x+1)
                c[i], c[x] = c[x], c[i]

        recur(0)
        return res
