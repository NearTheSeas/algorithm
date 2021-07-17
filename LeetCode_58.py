""" 
https://leetcode-cn.com/problems/length-of-last-word/
58. 最后一个单词的长度
倒序搜索
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #计算字符串的长度
        n = len(s)
        #计算最后单词的长度，初值为0
        nums = 0
        #从右向左遍历字符串
        for i in range(n-1,-1,-1):
            #当遍历到的值不为空格时，单词长度+1
            if s[i] != " ":
                nums += 1
            #当遍历到空格时，判断nums是否为0
            else:
                #nums不为0，说明已经遍历完了最后一个单词
                if nums != 0:
                    return nums
                #为0说明还没有遍历到字母
                else:
                    pass
        #如果没有单词返回初值
        return nums
