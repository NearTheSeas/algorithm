""" 
https://leetcode-cn.com/problems/jump-game/
55. 跳跃游戏
"""
from typing import List


class Solution:    
    def canJump(self, nums: List[int]) -> bool:
        far, n  = 0, len(nums)
        for i,num in enumerate(nums):
            print(i,num)
            if i <= far:
                far = max(i+num, far)
                if far >= n - 1:
                    return True
        return False
