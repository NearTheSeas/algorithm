""" 
https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
剑指 Offer 58 - II. 左旋转字符串
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)

    def reverseLeftWords(self, s: str, n: int) -> str:
        def reverse(i, j):
            while i < j:
                str_list[i], str_list[j] = str_list[j], str_list[i]
                i += 1
                j -= 1
        str_list = list(s)
        reverse(0, n-1)
        reverse(n, len(s)-1)
        reverse(0, len(s)-1)
        return ''.join(str_list)
