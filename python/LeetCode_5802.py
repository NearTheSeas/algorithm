""" 
https://leetcode-cn.com/problems/count-good-numbers/
5802. 统计好数字的数目

pow的用法 第三个参数
奇偶数的计算
"""


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        od = n >> 1
        ev = n - od
        ans = pow(5, ev, 1000000007) * pow(4, od, 1000000007) % 1000000007
        return ans
