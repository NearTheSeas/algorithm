""" 
https://leetcode-cn.com/problems/split-array-largest-sum/
410. 分割数组的最大值

由题意可知：子数组的最大值是有范围的，即在区间 [max(nums),sum(nums)]之中。
令 l=max(nums)，h=sum(nums)，mid=(l+h)/2，计算数组和最大值不大于mid对应的子数组个数 cnt(这个是关键！)
如果 cnt>m，说明划分的子数组多了，即我们找到的 mid 偏小，故 l=mid+1；
否则，说明划分的子数组少了，即 mid 偏大(或者正好就是目标值)，故 h=mid。

"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 判断子数组和的最大值为 x 划分的数组是否小于m
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            print(mid)  # 21 15 18 17 18
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def splitArray2(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[float('inf')]*(m+1) for _ in range(n+1)]
        sub = [0]  # 前缀和
        for num in nums:
            sub.append(sub[-1]+num)

        dp[0][0] = 0
        for i in range(1, n+1):  # 前i个数
            for j in range(1, min(i, m)+1):  # 分成不超过m个子数组
                for k in range(i): # K个数 分割成j-1段， sub[i]-sub[k]是最后一段的和
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i]-sub[k]))
        return dp[-1][-1]
