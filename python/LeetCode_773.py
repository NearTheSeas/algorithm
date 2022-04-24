""" 
https://leetcode-cn.com/problems/sliding-puzzle/
773. 滑动谜题
记录二位数组中可移动的下标位置
[0,1,2]
[3,4,5]
找到当前“0”所在位置，遍历其邻居
广度优先遍历
"""
from typing import List
import collections


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neighbours = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        state = "".join(str(c) for c in board[0]+board[1])
        start = state.index('0')
        visited = set()
        # (0的位置，当前字符串，步数)
        q = collections.deque([(start, state, 0)])
        while q:
            cur, state, steps = q.popleft()
            if state == '123450':
                return steps
            elif state in visited:
                continue
            else:
                visited.add(state)
                for nxt in neighbours[cur]:
                    tmp = list(state)
                    tmp[cur], tmp[nxt] = tmp[nxt], tmp[cur]
                    tmp = "".join(tmp)
                    q.append((nxt, tmp, steps+1))
        return -1
