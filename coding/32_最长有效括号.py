'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

解题思路：
利用栈保存“位置值”
base case :stack=[-1]

左括号入栈
右括号出栈
    出栈后为空时，入栈当前位置值,以保证栈顶表示的是有效括号起始位置的前一个位置（说明之前没有左括号匹配）
    出栈后不为空时，max_len=max(当前位置值-栈顶位置值,max_len)

tips:手动模拟更清楚

TODO：
dp
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #TODO dp
        stack=[-1]
        max_len=0
        for i_index,ichar in enumerate(s):
            if ichar=='(':
                stack.append(i_index)
            else:
                stack.pop(-1)
                if len(stack)==0:
                    stack.append(i_index)
                else:
                    max_len=max(max_len,i_index-stack[-1])
        return max_len

