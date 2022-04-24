""" 
https://leetcode-cn.com/problems/nim-game/
292. Nim 游戏
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
