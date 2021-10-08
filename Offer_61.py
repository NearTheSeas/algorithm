""" 
https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
剑指 Offer 61. 扑克牌中的顺子

顺子的条件 
    最小值和最大值的差值 不能超过5 
    除大小王，不能有重复的值
    
"""

from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        maxVal, minVal = 0, 14
        for num in nums:
            if num == 0:
                continue
            maxVal = max(maxVal, num)
            minVal = min(minVal, num)
            if num in repeat:
                return False
            repeat.add(num)
        return maxVal - minVal < 5
    
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子

