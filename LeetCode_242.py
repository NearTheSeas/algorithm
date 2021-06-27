""" 
https://leetcode-cn.com/problems/valid-anagram/
有效的字母异位词  字母出现的次数一样，顺序不一样
串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

输入: s = "anagram", t = "nagaram"
输出: true

注意预判字符长度是否相等
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = dict()
        for i in s:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        for j in t:
            if j in map and map[j] != 0:
                map[j]-=1
            else:
                return False
        return True