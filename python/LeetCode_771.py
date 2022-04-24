""" 
https://leetcode-cn.com/problems/jewels-and-stones/
771. 宝石与石头
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsSet = set(jewels)
        return sum(s in jewelsSet for s in stones)
