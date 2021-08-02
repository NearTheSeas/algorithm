""" 
https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree/
1104. 二叉树寻路

求label在这一行里的对称节点，label和它的对称节点sym_label之和为 (2**row-1+2**(row-1)) 
每个之字形label的父节点，就是label的sym_label在非之字形树里的父节点
"""
from typing import List
from math import log2


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        row = int(log2(label))+1
        ans = [0]*row
        while row:
            ans[row-1] = label
            label = (2**row-1-label+2**(row-1))//2
            row -= 1

        return ans
