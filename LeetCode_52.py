""" 
https://leetcode-cn.com/problems/n-queens-ii/
52. N皇后 II
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens:List[int], xy_dif:List[int], xy_sum:List[int]):
            p = len(queens)
            if p == n:
                result.append(queens) 
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    dfs(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        dfs([],[],[])
        return len(result)
