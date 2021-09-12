"""
https://leetcode-cn.com/problems/3sum/
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

先排序
第一个数的最大范围是n-2,
如果第一个数取值已经大于0  则退出
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    if not nums or n <= 2:
        return []
    result = []
    nums.sort()
    target = 0
    for k in range(n-2):
        if nums[k] > 0:
            return result
        if k > 0 and nums[k] == nums[k-1]:  # k > 0时 开始考虑去重
            continue
        i, j = k + 1, n-1
        while i < j:
            s = nums[k] + nums[i] + nums[j]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                result.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                # 去重
                while i < j and nums[i] == nums[i+1]:
                    i += 1
                while i < j and nums[j] == nums[j-1]:
                    j -= 1
    return result
