""" 
https://leetcode-cn.com/problems/isomorphic-strings/
205. 同构字符串
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[i]) == t.index(t[i])  for i in range(len(s)))


