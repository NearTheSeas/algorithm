""" 
https://leetcode-cn.com/problems/sqrtx/
69. x 的平方根
"""


class Solution():
    def mySqrt(self, x):
        l, r, ans = 1, x, -1
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
