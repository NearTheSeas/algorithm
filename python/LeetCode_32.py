""" 
https://leetcode-cn.com/problems/longest-valid-parentheses/
32. 最长有效括号
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 栈顶记录最后一个未匹配的括号
        stack, result = [(-1, ')')], 0
        for i, paren in enumerate(s):
            if paren == ')' and stack[-1][1] == '(':
                stack.pop()
                result = max(result, i - stack[-1][0])
            else:
                stack += (i, paren),
        return result

    def longestValidParentheses2(self, s: str) -> int:
        dp = [0] * len(s)
        ans = 0
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                # 前一个括号有匹配对
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == "(":
                    if dp[i-1] > 0:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                    else:
                        dp[i] = 0
                ans = max(ans, dp[i])
        return ans
