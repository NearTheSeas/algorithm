""" 
https://leetcode-cn.com/problems/walking-robot-simulation/
874. 模拟行走机器人
i=0,向北
i=1,向东
i=2,向南
i=3,向西
int direx[] = {0,1,0,-1};
int direy[] = {1,0,-1,0};
direx[],direy[] 要竖着对齐看
    - 向北，坐标轴上x不动，y+1, 即(0,1)
    - 向东，坐标轴上x+1，y不动, 即(1,0)
    - 向南，坐标轴上x不动，y-1, 即(0,-1)
    - 向西，坐标轴上x-1，y不动, 即(-1,0)
"-1"：“向右转90度”，只要当前方向curdire + 1就可以得到右转方向
"-2"：“向左转90度”，只要当前方向curdire + 3 就可以得到左转方向 (curdire + 3) % 4，
因为不管curdire当前是哪个方向，左转都在其左边，在direx数组的定义中顺势针数3个就是其左边，所以就是加3

"""
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0
        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)
        return ans
