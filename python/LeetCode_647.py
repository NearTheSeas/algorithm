""" 
https://leetcode-cn.com/problems/palindromic-substrings/
647. 回文子串

回文判断：中心拓展
中心点不能只有单个字符构成，还要包括两个字符，
比如上面这个子串 abab，就可以有中心点 ba 扩展一次得到，
所以最终的中心点由 2 * len - 1 个，分别是 len 个单字符和 len - 1 个双字符

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            ans += self.extend(s, i, i, n)
            ans += self.extend(s, i, i+1, n)

        return ans

    def extend(self, s, i, j, n):
        ans = 0
        while i >= 0 and j < n and s[i] == s[j]:
            ans += 1
            i -= 1
            j += 1
        return ans

    def countSubstrings2(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1:
                        ans += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        ans += 1
                        dp[i][j] = True
        return ans
