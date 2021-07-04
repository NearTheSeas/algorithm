""" 
https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
45. 跳跃游戏 II
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # maxPos 是遍历到end时，中间节点可以到达的最远位置
        # end 是当前次的跳转可以到达的最远位置
        maxPos, end, step = 0, 0, 0
        for i in range(n-1):
            if maxPos >= i:
                maxPos = max(maxPos, i+nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
