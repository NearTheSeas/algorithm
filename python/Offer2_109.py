"""
https://leetcode-cn.com/problems/zlDJc7/
剑指 Offer II 109. 开密码锁
双向BFS
"""
from typing import List
# import collections


class Solution:
    def plusOne(self, state, i): #拷贝自@lanmo2018 数字+1 注意否溢出 9 → 0
        retate_num = ''
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if state[i] >= '0' and state[i] < '9':
            retate_num = state[:i] + nums[int(state[i]) + 1] + state[i+1:]
        else:
            retate_num = state[:i] + '0' + state[i + 1:]
        return retate_num

    def minusOne(self, state, i): #拷贝自@lanmo2018 数字-1 注意是否溢出 0 → 9
        retate_num = ''
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if state[i] > '0' and state[i] <= '9':
            retate_num = state[:i] + nums[int(state[i]) - 1] + state[i + 1:]
        else:
            retate_num = state[:i] + '9' + state[i + 1:]
        return retate_num

    def openLock(self, deadends: List[str], target: str) -> int:
        starter = '0000'
        if starter in deadends:
            return -1
        if target == starter:
            return 0

        # 双向BFS 
        # 仅使用一个 visited
        # set的查找速度更快
        steps = 0
        front = set([starter])
        end = set([target])
        visited = set(deadends) 
        visited.add(starter)
        while front and end:
            steps += 1
            tmp = set()
            for item in front:
                for i in range(4):
                    plus_num = self.plusOne(item, i)
                    minus_num = self.minusOne(item, i)
                    if plus_num in end or minus_num in end: # 转换之后恰好在另一个结果集中，说明找到答案
                        return steps
                    if plus_num not in visited: # 避免重复遍历
                        tmp.add(plus_num)
                        visited.add(plus_num)
                    if minus_num not in visited:
                        tmp.add(minus_num)
                        visited.add(minus_num)
             # 小优化，每次都是从font扩散遍历，因此front越小 遍历的越少
            front = tmp
            if len(front) > len(end):
                front, end = end, front # 互换位置，front是较小那个
        return - 1
