""" 
https://leetcode-cn.com/problems/QA2IGt/
剑指 Offer II 113. 课程顺序
"""
from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegrees = [0]*numCourses

        for cl2, cl1 in prerequisites:
            graph[cl1].append(cl2)
            indegrees[cl2] += 1

        q = collections.deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for neighbour in graph[cur]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    q.append(neighbour)

        return res if len(res) == numCourses else []
