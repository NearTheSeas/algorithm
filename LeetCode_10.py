""" 
https://leetcode-cn.com/problems/regular-expression-matching/
10. 正则表达式匹配

用 f[i][j] 表示 s 的前 i 个字符与 p 中的前 j 个字符是否能够匹配
p[j]：
    可能是字母
    可能是* 
    可能是. 
如果 p[j] == s[i] : dp[i][j] = dp[i-1][j-1]；
如果 p[j] == '.' : dp[i][j] = dp[i-1][j-1]；
如果 p[j] == '*'：
    如果 p[j-1] != s[i] : dp[i][j] = dp[i][j-2] //in this case, a* only counts as empty
    如果 p[j-1] == s[i] or p[j-1] == '.'：
        dp[i][j] = dp[i-1][j] //in this case, a* counts as multiple a
        or dp[i][j] = dp[i][j-1] // in this case, a* counts as single a
        or dp[i][j] = dp[i][j-2] // in this case, a* counts as empty

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]

        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == "*":
                    dp[i][j] |= dp[i][j-2]
                    if matches(i, j-1):
                        dp[i][j] |= dp[i-1][j]
                else:
                    if matches(i, j):
                        dp[i][j] |= dp[i-1][j-1]
        return dp[m][n]
