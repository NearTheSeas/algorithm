""" 
https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
剑指 Offer 39. 数组中出现次数超过一半的数字
"""


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = None
        counter = 0
        for num in nums:
            if not res:
                res = num
                counter = 1
            else:
                if num != res:
                    counter -= 1
                    if counter < 0:
                        res = num
                        counter = 1
                else:
                    counter += 1
        return res

    def majorityElement(self, nums: List[int]) -> int:
        res, counter = None, 0

        for num in nums:
            if counter == 0:
                res = num
            counter += 1 if num == res else -1
        return res
