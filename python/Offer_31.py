""" 
https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
剑指 Offer 31. 栈的压入、弹出序列
"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack
