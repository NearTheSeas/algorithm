"""
https://leetcode-cn.com/problems/plus-one/
加一
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

"""
from types import List


def plusOne(digits: List[int]) -> List[int]:
    if not digits:
        return []
    n = len(digits)-1
    while n >= 0:
        digits[n] = (digits[n] + 1) % 10
        if digits[n] != 0:
            return digits
        n -= 1
    digits.insert(0, 1)
    return digits
