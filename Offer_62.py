""" 
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
剑指 Offer 62. 圆圈中最后剩下的数字

(idx + m -1) mod n 
"""


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n+1):
            x = (x+m) % i
        return x
