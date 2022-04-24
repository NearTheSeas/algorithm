""" 
https://leetcode-cn.com/problems/valid-parentheses/
有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

如果字符串为奇数 false
遍历字符串 如果得到的是右括号，判断是否与栈顶匹配 否 False   是 pop
            如果是左括号 入栈
            
注意点：
1. 判断字符串是否为奇数
2. 可以入栈左括号 也可以入栈右括号 匹配的时候需要区分
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) % 2 == 1:
            return False

        pairs = {
            "(": ")",
            "[": ']',
            '{': '}'
        }
        stack = []
        for ch in s:
            if ch not in pairs:
                if not stack or stack[-1] != ch:
                    return False
                stack.pop()
            else:
                stack.append(pairs[ch])
        return not stack
