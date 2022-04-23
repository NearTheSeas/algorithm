""" 
https://leetcode-cn.com/problems/jJ0w9p/
剑指 Offer II 072. 求平方根
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid**2 <= x:
                if (mid+1)**2 > x:
                    return mid
                left = mid + 1
            else:
                right = mid - 1
        return 0
