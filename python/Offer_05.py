""" 
https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
剑指 Offer 05. 替换空格
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        arr = list(s)
        for i, ch in enumerate(arr):
            if ch == " ":
                arr[i] = '%20'

        return ''.join(x for x in arr)
