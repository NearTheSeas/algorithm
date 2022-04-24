""" 
https://leetcode-cn.com/problems/valid-perfect-square/
367. 有效的完全平方数
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
