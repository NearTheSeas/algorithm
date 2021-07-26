"""
https://leetcode-cn.com/problems/task-scheduler/
621. 任务调度器

不断遍历任务 找到剩余任务数最大 且 不在冷却期的任务来执行
在迭代时间点的时候 跳过冷却期

用二元组 (nextValid_i, rest_i) 表示第 i 个任务，其中 nextValid_i 表示其因冷却限制，
最早可以执行的时间； rest_i 表示其剩余执行次数。初始时，所有的 nextValid_i表示其因冷却限制，均为 1，
rest_i 即为任务 i 在数组tasks 中出现的次数

选择不在冷却中并且剩余执行次数最多的那个任务
将 (nextValid_i, rest_i) 更新为 (time+n+1, rest_i-1)

"""
from typing import List
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        maxExec = max(freq.values())  # 最多的执行次数
        maxCnt = sum(1 for v in freq.values() if v == maxExec)  # 具有最多执行次数的任务数量
        return max((maxExec - 1)*(n+1) + maxCnt, len(tasks))

    def leastInterval2(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        n = len(freq)
        nextValid = [1] * n  # 表示其因冷却限制，最早可以执行的时间
        rest = list(freq.values())  # 剩余执行次数
        time = 0  # 当前时间
        # 选择不在冷却中并且剩余执行次数最多的那个任务
        for _ in range(len(tasks)):
            time += 1
            minNextValid = min(nextValid[j] for j in range(n) if rest[j] > 0)
            time = max(time, minNextValid)

            best = -1
            for j in range(n):
                if rest[j] and nextValid[j] <= time:  # 任务类型j 还有可执行次数 且冷却期在time范围内
                    if best == -1 or rest[j] > rest[best]:  # 保留剩余任务数量最大的
                        best = j
        nextValid[best] = time + n + 1  # 更新任务的下一执行时间
        rest[best] -= 1
        return time
