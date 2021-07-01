""" 
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
17. 电话号码的字母组合
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []

        def backtrack(index: int, strList: List) -> None:
            if index == len(digits):
                result.append("".join(strList))
                return
            digit = digits[index]
            for letter in phoneMap[digit]:
                strList.append(letter)
                backtrack(index + 1, strList)
                strList.pop()

        backtrack(0, [])
        return result
