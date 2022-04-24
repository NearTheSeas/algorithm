""" 
https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/
剑指 Offer 43. 1～n 整数中 1 出现的次数
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        hight, cur, low = n//10, n % 10, 0
        while hight != 0 or cur != 0:
            if cur == 0:
                res += hight * digit
            elif cur == 1:
                res += hight * digit + low + 1
            else:
                res += (hight + 1) * digit
            low += cur * digit
            cur = hight % 10
            hight //= 10
            digit *= 10
        return res
