""" 
https://leetcode-cn.com/problems/to-lower-case/
709. 转换成小写字母

字母位运算技巧
大写变小写、小写变大写：字符 ^= 32 （大写 ^= 32 相当于 +32，小写 ^= 32 相当于 -32）
大写变小写、小写变小写：字符 |= 32 （大写 |= 32 就相当于+32，小写 |= 32 不变）
大写变大写、小写变大写：字符 &= -33 （大写 ^= -33 不变，小写 ^= -33 相当于 -32）

"""


class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ""
        for s in str:
            if s >= 'A' and s <= 'Z':
                s = chr(ord(s) + 32)
            result += s
        return result
