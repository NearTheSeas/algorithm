"""
https://leetcode-cn.com/problems/move-zeroes/

key: 一维数组坐标变换 双指针
desc:给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
input: nums
output: nums
test: [], [1,2,3], [0,0,0,0] , [1,0,3,4]
"""
from typing import List


def moveZeros(nums: List[int]) -> None:
    # 异常输入判断
    if not nums:
        return []
    # 遍历数组找到非0元素 与前面的元素互换位置
    pos = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1
