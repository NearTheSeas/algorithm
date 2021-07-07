from LeetCode_410 import Solution

from typing import List


# class Solution:
#     def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
#         n, counter = len(dist), 0
#         rounds = [dist[i]/speed[i] for i in range(n)]
#         rounds.sort()
#         for i in range(n):
#             if rounds[i] > i:
#                 counter += 1
#             else:
#                 return counter
#         return counter


if __name__ == '__main__':

    s = Solution()
    r = s.splitArray([7,2,5,10,8],2)
    print(r)


# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# 输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# 解释：存在 2 种最短的转换序列：
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
