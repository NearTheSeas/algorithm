""" 
https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/
剑指 Offer 67. 把字符串转换成整数

在每轮数字拼接前，判断 resres 在此轮拼接后是否超过 21474836472147483647 
若超过则加上符号位直接返回。
设数字拼接边界 bndry = 2147483647 // 10 = 214748364

"""


class Solution:
    def strToInt(self, str: str) -> int:
        res, i, sign, length = 0, 0, 1, len(str)
        int_max, int_min, bndry = 2**31 - 1, -2**31, 2**31 // 10
        if not str:
            return 0
        while str[i] == ' ':
            i += 1
            if i == length:
                return 0
        if str[i] == '-':
            sign = -1
        if str[i] in '+-':
            i += 1
        for c in str[i:]:
            if not '0' <= c <= '9':
                break
            if res > bndry or res == bndry and c > '7':
                return int_max if sign == 1 else int_min
            res = 10 * res + ord(c) - ord('0')
        return sign * res
