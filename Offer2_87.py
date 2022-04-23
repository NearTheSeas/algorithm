""" 
https://leetcode-cn.com/problems/0on3uN/
剑指 Offer II 087. 复原 IP 
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        res = []

        def helper(idx, path):
            if idx == n and len(path) == 4:
                res.append(path[:])
                return
            if len(path) > 4:
                return

            for i in range(idx, n):
                seg = s[idx: i+1]
                if int(seg) < 256 and len(seg) == len(str(int(seg))):
                    helper(i+1, path + [seg])
        helper(0, [])
        return ['.'.join(item) for item in res]
