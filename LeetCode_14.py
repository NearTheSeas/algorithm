""" 
https://leetcode-cn.com/problems/longest-common-prefix/description/
14. 最长公共前缀

"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i== len(strs[j]) or strs[j][i] !=c for j in range(1,count)):
                return strs[0][:i]

        return strs[0]
